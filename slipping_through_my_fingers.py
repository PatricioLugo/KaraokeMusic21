# Patricio Lugo A01707192 - Claudio López A01710963
from music21 import note, clef, chord, instrument, stream, metadata, key
import note_insertion1

# Stream and stream parts creation
s = stream.Stream(id = 'stream')
s.insert(0, metadata.Metadata(title = 'Slipping Through My Fingers'))
violoncelloPart = stream.Part(id = 'violoncelloPart')
acGuitar1 = stream.Part(id = 'acGuitarPart1')
acGuitar2 = stream.Part(id = 'acGuitarPart2')

# Measure creation
note_insertion1.m01(violoncelloPart)
note_insertion1.m02(violoncelloPart)
note_insertion1.m03(violoncelloPart)
note_insertion1.m04(violoncelloPart)
note_insertion1.m05(violoncelloPart)
note_insertion1.m06(violoncelloPart)
note_insertion1.m07(violoncelloPart)
note_insertion1.m08(violoncelloPart)
note_insertion1.m09(violoncelloPart)
note_insertion1.m010(violoncelloPart)
note_insertion1.m011(violoncelloPart)
note_insertion1.m012(violoncelloPart)
note_insertion1.m013(violoncelloPart)
note_insertion1.m014(violoncelloPart)
note_insertion1.m015(violoncelloPart)
note_insertion1.m016(violoncelloPart)
note_insertion1.m017(violoncelloPart)
note_insertion1.m018(violoncelloPart)
note_insertion1.m019(violoncelloPart)
note_insertion1.m020(violoncelloPart)
note_insertion1.m021(violoncelloPart)
note_insertion1.m022(violoncelloPart)
note_insertion1.m023(violoncelloPart)
note_insertion1.m024(violoncelloPart)
note_insertion1.m025(violoncelloPart)
note_insertion1.m026(violoncelloPart)

s.insert(0, violoncelloPart)
clef.bestClef(s, allowTreble8vb=True)
s.show()