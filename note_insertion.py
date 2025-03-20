from music21 import note, clef, chord, instrument, stream

def m1(part_):

    d = note.Note('D')
    d.duration.quarterLength = 2
    d.insertLyric('school')
    part_.append(d)

    d2 = note.Note('D')
    d2.insertLyric('bag')
    part_.append(d2)

    e = note.Note('E')
    e.duration.quarterLength = 0.5
    e.insertLyric('in')
    part_.append(e)

    f = note.Note('F')
    f.duration.quarterLength = 1.5
    f.insertLyric('hand,_')
    part_.append(f)

def m2(part_):

    r = note.Rest()
    r.duration.quarterLength = 1
    part_.append(r)

    f = note.Note('F')
    f.insertLyric('she')
    part_.append(f)

    g = note.Note('G')
    g.insertLyric('leaves')
    part_.append(g)