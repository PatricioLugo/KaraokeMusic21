from music21 import note, clef, chord, instrument, stream, metadata
import note_insertion

# Stream and stream parts creation
s = stream.Stream(id = 'stream')
s.insert(0, metadata.Metadata(title = 'Slipping Through My Fingers'))
violoncelloPart = stream.Part(id = 'violoncelloPart')
acGuitar1 = stream.Part(id = 'acGuitarPart1')
acGuitar2 = stream.Part(id = 'acGuitarPart2')

# Measure creation
note_insertion.m1(violoncelloPart)
note_insertion.m2(violoncelloPart)

s.insert(0, violoncelloPart)
clef.bestClef(s, allowTreble8vb=True)
s.show()