import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pygame
import music21
from music21 import converter, note, stream, chord
import os
import tempfile
import threading
import time

class LyricViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Letras Musicales")
        self.root.geometry("800x600")
        self.root.configure(padx=20, pady=20)
        
        # Initialize pygame mixer
        pygame.mixer.init(frequency=44100)
        
        # Variables
        self.archivo_nombre = tk.StringVar()
        self.current_lyric = tk.StringVar(value="")
        self.next_lyric = tk.StringVar(value="")
        self.partitura = None
        self.lyric_notes = []
        self.current_index = 0
        self.playing = False
        self.temp_midi_file = None
        self.playback_thread = None
        self.lyric_update_thread = None
        self.duration = 0
        
        # Create interface
        self.crear_interfaz()
        
        # When closing the window, ensure pygame is properly shut down
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def crear_interfaz(self):
        # File selection frame
        frame_archivo = ttk.LabelFrame(self.root, text="Archivo MIDI o MusicXML")
        frame_archivo.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(frame_archivo, text="Archivo:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(frame_archivo, textvariable=self.archivo_nombre, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame_archivo, text="Examinar", command=self.cargar_archivo).grid(row=0, column=2, padx=5, pady=5)
        
        # Lyrics display frame
        frame_lyrics = ttk.LabelFrame(self.root, text="Visualización de Letras")
        frame_lyrics.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Current lyric (large font)
        self.current_lyric_label = tk.Label(frame_lyrics, textvariable=self.current_lyric, 
                                        font=("Arial", 32, "bold"), wraplength=700,
                                        height=3, bg="#f0f0f0", fg="#000000")
        self.current_lyric_label.pack(fill="x", pady=20)
        
        # Next lyric (smaller font)
        ttk.Label(frame_lyrics, text="Siguiente:").pack(anchor="w", padx=5)
        ttk.Label(frame_lyrics, textvariable=self.next_lyric, font=("Arial", 16)).pack(anchor="w", padx=5)
        
        # Full lyrics display
        ttk.Label(frame_lyrics, text="Letra completa:").pack(anchor="w", padx=5, pady=(20, 5))
        
        frame_full_lyrics = ttk.Frame(frame_lyrics)
        frame_full_lyrics.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Scrollable text widget for full lyrics
        self.full_lyrics_text = tk.Text(frame_full_lyrics, height=10, wrap="word", font=("Arial", 12))
        scrollbar = ttk.Scrollbar(frame_full_lyrics, command=self.full_lyrics_text.yview)
        self.full_lyrics_text.configure(yscrollcommand=scrollbar.set)
        
        self.full_lyrics_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Playback controls
        frame_controls = ttk.Frame(self.root)
        frame_controls.pack(fill="x", padx=10, pady=10)
        
        self.btn_play = ttk.Button(frame_controls, text="Reproducir", command=self.reproducir)
        self.btn_play.pack(side="left", padx=5)
        
        self.btn_stop = ttk.Button(frame_controls, text="Detener", command=self.detener_reproduccion, state="disabled")
        self.btn_stop.pack(side="left", padx=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(frame_controls, variable=self.progress_var, maximum=100, length=300)
        self.progress_bar.pack(side="left", padx=20, fill="x", expand=True)
    
    def cargar_archivo(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo musical",
            filetypes=(("Archivos MIDI", "*.mid *.midi"), 
                      ("Archivos MusicXML", "*.xml *.musicxml"),
                      ("Todos los archivos", "*.*"))
        )
        
        if archivo:
            try:
                self.archivo_nombre.set(archivo)
                
                # Cargar archivo con music21
                self.partitura = converter.parse(archivo)
                
                # Extract lyrics from the score and prepare for display
                self.extract_lyrics()
                
                # Display full lyrics in the text widget
                self.display_full_lyrics()
                
                messagebox.showinfo("Éxito", f"Archivo cargado correctamente: {os.path.basename(archivo)}")
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
    
    def extract_lyrics(self):
        """Extract lyrics and their associated notes from the score"""
        self.lyric_notes = []
        
        # Get all parts from the score
        parts = self.partitura.getElementsByClass('Part')
        if not parts:
            # If no parts found, try to get notes directly
            parts = [self.partitura]
        
        # Determine the tempo (bpm) from the score if available
        self.tempo = 120  # Default tempo
        for metronome in self.partitura.flatten().getElementsByClass('MetronomeMark'):
            self.tempo = metronome.number
            break
        
        # Calculate seconds per quarter note based on tempo
        self.seconds_per_quarter = 60 / self.tempo
        
        # Calcular offset total para todas las notas
        for part in parts:
            # Look for notes with lyrics in each part
            for element in part.flatten().notesAndRests:
                # Calcular offset absoluto en la partitura
                absolute_offset = element.getOffsetBySite(part.flatten())
                
                if isinstance(element, note.Note) and element.lyric is not None and element.lyric.strip():
                    # Solo añadir si hay una letra real (no vacía)
                    self.lyric_notes.append({
                        'note': element,
                        'lyric': element.lyric,
                        'offset': absolute_offset,
                        'duration': element.duration.quarterLength
                    })
                elif isinstance(element, chord.Chord):
                    # Check if any note in the chord has a lyric
                    for n in element.notes:
                        if n.lyric is not None and n.lyric.strip():
                            self.lyric_notes.append({
                                'note': n,
                                'lyric': n.lyric,
                                'offset': absolute_offset,
                                'duration': element.duration.quarterLength
                            })
        
        # Sort by offset time
        self.lyric_notes.sort(key=lambda x: x['offset'])
        
        # Initialize display
        self.current_index = 0
        self.update_lyric_display()
    
    def display_full_lyrics(self):
        """Display the full lyrics in the text widget"""
        self.full_lyrics_text.delete(1.0, tk.END)
        
        if not self.lyric_notes:
            self.full_lyrics_text.insert(tk.END, "No se encontraron letras en este archivo.")
            return
        
        # Combine consecutive lyric segments into lines
        current_line = ""
        line_list = []
        
        for item in self.lyric_notes:
            lyric = item['lyric']
            
            # Check if this lyric should start a new line
            if lyric.endswith('\n') or lyric.endswith('/') or lyric.endswith('//'):
                # Remove line break markers
                clean_lyric = lyric.replace('\n', '').replace('/', '')
                current_line += clean_lyric
                line_list.append(current_line.strip())
                current_line = ""
            else:
                current_line += lyric + " "
        
        # Add the last line if it exists
        if current_line:
            line_list.append(current_line.strip())
        
        # Display lines in the text widget
        for line in line_list:
            self.full_lyrics_text.insert(tk.END, line + "\n")
    
    def update_lyric_display(self):
        """Update the current and next lyric display"""
        if not self.lyric_notes:
            self.current_lyric.set("No hay letras disponibles")
            self.next_lyric.set("")
            return
        
        if self.current_index < len(self.lyric_notes):
            # Set current lyric
            current = self.lyric_notes[self.current_index]['lyric']
            self.current_lyric.set(current)
            
            # Set next lyric if available
            if self.current_index + 1 < len(self.lyric_notes):
                next_lyric = self.lyric_notes[self.current_index + 1]['lyric']
                self.next_lyric.set(next_lyric)
            else:
                self.next_lyric.set("")
        else:
            self.current_lyric.set("Fin de la canción")
            self.next_lyric.set("")
    
    def create_temp_midi(self):
        """Create a temporary MIDI file from the score"""
        if self.temp_midi_file:
            try:
                # Remove previous temp file if it exists
                if os.path.exists(self.temp_midi_file):
                    os.remove(self.temp_midi_file)
            except:
                pass
        
        # Create new temp file
        fd, temp_path = tempfile.mkstemp(suffix='.mid')
        os.close(fd)
        
        self.partitura.write('midi', fp=temp_path)
        self.temp_midi_file = temp_path
        return temp_path
    
    def update_progress_bar(self):
        """Update the progress bar during playback"""
        start_time = time.time()
        self.progress_var.set(0)
        
        while self.playing and pygame.mixer.music.get_busy():
            elapsed = time.time() - start_time
            if elapsed < self.duration:
                progress = (elapsed / self.duration) * 100
                self.progress_var.set(progress)
            else:
                break
            time.sleep(0.1)
            
        if self.playing:  # If playback ended naturally
            self.playing = False
            self.progress_var.set(100)
            self.root.after(500, self.reset_playback)
        
    def sync_lyrics(self):
        """Synchronize lyrics with music playback using absolute timing"""
        if not self.lyric_notes:
            return
            
        start_time = time.time()
        self.current_index = 0
        self.update_lyric_display()
        
        # Tiempo base para la sincronización
        seconds_per_quarter = self.seconds_per_quarter
        
        while self.playing and self.current_index < len(self.lyric_notes):
            current_item = self.lyric_notes[self.current_index]
            
            # Calcular tiempo absoluto cuando esta nota debe mostrarse
            current_offset = current_item['offset']
            absolute_time = start_time + (current_offset * seconds_per_quarter)
            
            # Esperar hasta que sea el momento exacto de mostrar esta letra
            now = time.time()
            if now < absolute_time:
                time.sleep(absolute_time - now)
            
            # Mostrar la letra actual
            self.root.after(0, self.update_lyric_display)
            
            # Calcular tiempo para la próxima nota
            if self.current_index + 1 < len(self.lyric_notes):
                next_item = self.lyric_notes[self.current_index + 1]
                next_offset = next_item['offset']
                
                # Avanzar al siguiente lyric cuando sea el momento
                self.current_index += 1
                
                # Si hay un salto grande entre notas, establecer un tiempo máximo de espera
                time_to_next = (next_offset - current_offset) * seconds_per_quarter
                if time_to_next > 0.1:  # Tiempo mínimo para evitar avances demasiado rápidos
                    time.sleep(time_to_next)
            else:
                # Última nota, mostrarla por su duración
                duration_seconds = current_item['duration'] * seconds_per_quarter
                time.sleep(max(0.5, duration_seconds))
                self.current_index += 1
                
        if self.playing:
            # Mostrar "Fin de la canción" cuando termina
            self.root.after(0, lambda: self.current_lyric.set("Fin de la canción"))
            self.root.after(0, lambda: self.next_lyric.set(""))
        
    def estimate_duration(self):
        """Estimate the duration of the score in seconds"""
        if self.partitura.highestTime > 0:
            return self.partitura.highestTime * 1.2  # Add 20% margin
        return 60  # Default 60 seconds if cannot determine
    
    def reproducir(self):
        """Play the score and show synchronized lyrics"""
        if not self.partitura:
            messagebox.showerror("Error", "Primero debe cargar un archivo musical")
            return
        
        try:
            if self.playing:
                self.detener_reproduccion()
                
            midi_path = self.create_temp_midi()
            self.duration = self.estimate_duration()
            
            pygame.mixer.music.load(midi_path)
            self.playing = True
            self.current_index = 0
            
            # Start playback
            pygame.mixer.music.play()
            
            # Update UI
            self.btn_play.state(['disabled'])
            self.btn_stop.state(['!disabled'])
            
            # Start threads for progress bar and lyric synchronization
            self.playback_thread = threading.Thread(target=self.update_progress_bar)
            self.playback_thread.daemon = True
            self.playback_thread.start()
            
            self.lyric_update_thread = threading.Thread(target=self.sync_lyrics)
            self.lyric_update_thread.daemon = True
            self.lyric_update_thread.start()
                
        except Exception as e:
            messagebox.showerror("Error de reproducción", f"No se pudo reproducir el archivo: {str(e)}")
            self.reset_playback()
    
    def detener_reproduccion(self):
        """Stop the current playback"""
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.reset_playback()
    
    def reset_playback(self):
        """Reset playback controls"""
        self.btn_play.state(['!disabled'])
        self.btn_stop.state(['disabled'])
        self.progress_var.set(0)
    
    def on_closing(self):
        """Clean up resources before closing the application"""
        self.detener_reproduccion()
        
        # Remove temp file if it exists
        if self.temp_midi_file and os.path.exists(self.temp_midi_file):
            try:
                os.remove(self.temp_midi_file)
            except:
                pass
        
        pygame.mixer.quit()
        pygame.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LyricViewer(root)
    root.mainloop()
