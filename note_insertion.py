from music21 import note, clef, chord, instrument, stream

def m01(part_):

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
    f.insertLyric('hand,')
    part_.append(f)

def m02(part_):

    r = note.Rest()
    r.duration.quarterLength = 1
    part_.append(r)

    f = note.Note('F')
    f.insertLyric('she')
    part_.append(f)

    g = note.Note('G')
    g.insertLyric('leaves')
    part_.append(g)

def m03(part_):

    a = note.Note('A')
    a.duration.quarterLength = 2
    a.insertLyric('home')
    part_.append(a)

    a2 = note.Note('A')
    a2.insertLyric('in')
    part_.append(a2)

    bflat = note.Note('Bb')
    bflat.duration.quarterLength = 0.5
    bflat.insertLyric('the')
    part_.append(bflat)

    a3 = note.Note('A')
    a3.duration.quarterLength = 1.5
    a3.insertLyric('ear')
    part_.append(a3)

def m04(part_):

    g = note.Note('G')
    g.duration.quarterLength = 0.5
    g.insertLyric('ly')
    part_.append(g)

    f = note.Note('F')
    f.duration.quarterLength = 1.5
    f.insertLyric('morn')
    part_.append(f)

    e = note.Note('E')
    e.insertLyric('ing')
    part_.append(e)

def m05(part_):

    r = note.Rest()
    r.duration.quarterLength = 2
    part_.append(r)

    d = note.Note('D')
    d.insertLyric('wav')
    part_.append(d)

    d2 = note.Note('D')
    d2.duration.quarterLength = 0.5
    d2.insertLyric('ing')
    part_.append(d2)

    e = note.Note('E')
    e.duration.quarterLength = 0.5
    e.insertLyric('good')
    part_.append(e)

def m06(part_):

    f = note.Note('F')
    f.insertLyric('bye')
    part_.append(f)

    r = note.Rest()
    part_.append(r)

    r2 = note.Rest()
    part_.append(r2)

    f2 = note.Note('F')
    f2.duration.quarterLength = 0.5
    f2.insertLyric('with')
    part_.append(f2)

    g = note.Note('G')
    g.duration.quarterLength = 0.5
    g.insertLyric('an')
    part_.append(g)

def m07(part_):

    bflat = note.Note('Bb')
    bflat.insertLyric('ab')
    part_.append(bflat)

    a = note.Note('A')
    a.insertLyric('sent')
    part_.append(a)

    g = note.Note('G')
    g.insertLyric('mind')
    part_.append(g)

    f = note.Note('F')
    f.insertLyric('ed')
    part_.append(f)

def m08(part_):

    a = note.Note('A')
    a.duration.quarterLength = 4
    a.insertLyric('smile')
    part_.append(a)

def m09(part_):

    d = note.Note('D')
    d.duration.quarterLength = 2
    d.insertLyric('I')
    part_.append(d)

    d2 = note.Note('D')
    d2.insertLyric('watch')
    part_.append(d2)

    e = note.Note('E')
    e.duration.quarterLength = 0.5
    e.insertLyric('her')
    part_.append(e)

    f = note.Note('F')
    f.duration.quarterLength = 1.5
    f.insertLyric('go')
    part_.append(f)

def m010(part_):

    r = note.Rest()
    r.duration.quarterLength = 2
    part_.append(r)

    f = note.Note('F')
    f.duration.quarterLength = 0.5
    f.insertLyric('with')
    part_.append(f)

    g = note.Note('G')
    g.duration.quarterLength = 0.5
    g.insertLyric('a')
    part_.append(g)

def m011(part_):

    a = note.Note('A')
    a.duration.quarterLength = 2
    a.insertLyric('surge')
    part_.append(a)

    a2 = note.Note('A')
    a2.insertLyric('of')
    part_.append(a2)

    bflat = note.Note('Bb')
    bflat.insertLyric('that')
    part_.append(bflat)

def m012(part_):

    a = note.Note('A')
    a.insertLyric('well')
    part_.append(a)

    g = note.Note('G')
    g.insertLyric('known')
    part_.append(g)

    f = note.Note('F')
    f.insertLyric('sad')
    part_.append(f)

    e = note.Note('E')
    e.insertLyric('ness')
    part_.append(e)

def m013(part_):

    r = note.Rest()
    part_.append(r)

    d = note.Note('D')
    d.duration.quarterLength = 0.5
    d.insertLyric('And')
    part_.append(d)

    bflat = note.Note('Bb')
    bflat.duration.quarterLength = 0.5
    bflat.insertLyric('I')
    part_.append(bflat)

    bflat2 = note.Note('Bb')
    bflat2.insertLyric('have')
    part_.append(bflat2)

    a = note.Note('A')
    a.duration.quarterLength = 0.5
    a.insertLyric('to')
    part_.append(a)

    a2 = note.Note('A')
    a2.duration.quarterLength = 1.5
    a2.insertLyric('sit')
    part_.append(a2)

def m014(part_):

    g = note.Note('G')
    g.insertLyric('down')
    part_.append(g)

    g2 = note.Note('G')
    g2.duration.quarterLength = 0.5
    part_.append(g2)

    g3 = note.Note('G')
    g3.duration.quarterLength = 0.5
    g3.insertLyric('for')
    part_.append(g3)

    f = note.Note('F')
    f.duration.quarterLength = 0.5
    f.insertLyric('a')
    part_.append(f)

    f2 = note.Note('F')
    f2.duration.quarterLength = 2.5
    f2.insertLyric('while')
    part_.append(f2)

def m015(part_):

    r  = note.Rest()
    r.duration.quarterLength = 3
    part_.append(r)

def m016(part_):

    r = note.Rest()
    r.duration.quarterLength = 2.5
    part_.append(r)

    d = note.Note('D')
    d.duration.quarterLength = 0.5
    d.insertLyric('The')
    part_.append(d)

def m017(part_):

    d = note.Note('D')
    d.duration.quarterLength = 0.5
    d.insertLyric('feel')
    part_.append(d)

    bflat = note.Note('Bb')
    bflat.duration.quarterLength = 2
    bflat.insertLyric('ing')
    part_.append(bflat)

    bflat2 = note.Note('Bb')
    bflat2.duration.quarterLength = 0.5
    bflat2.insertLyric('that')
    part_.append(bflat2)

    a = note.Note('A')
    a.insertLyric("I'm")
    part_.append(a)

def m018(part_):

    a = note.Note('A')
    a.duration.quarterLength = 0.5
    a.insertLyric('los')
    part_.append(a)

    g  = note.Note('G')
    g.insertLyric('ing')
    part_.append(g)

    g2 = note.Note('G')
    g2.duration.quarterLength = 1.5
    g2.insertLyric('her')
    part_.append(g2)

    c = note.Note('C')
    c.duration.quarterLength = 0.5
    c.insertLyric('for')
    part_.append(c)

    c2 = note.Note('C')
    c2.insertLyric('ev')
    part_.append(c2)

def m019(part_):
     
    a = note.Note('A')
    a.duration.quarterLength = 2.5
    a.insertLyric('er')
    part_.append(a)

    r = note.Rest()
    part_.append(r)

def m020(part_):

    r = note.Rest()
    r.duration.quarterLength = 3.5
    part_.append(r)

def small_seq(part_):

    c = note.Note('C')
    c.duration.quarterLength = 0.5
    part_.append(c)

    c2 = note.Note('C')
    part_.append(c2)

def b_dChord(part_, duration = 1):

    b_d = chord.Chord(['B3', 'D'])
    b_d.duration.quarterLength = duration
    part_.append(b_d)

def c_eChord(part_, duration = 1):

    c_e = chord.Chord(['C', 'E'])
    c_e.duration.quarterLength = duration
    part_.append(c_e)

def db_fChord(part_, duration = 1):

    db_f = chord.Chord(['Db', 'F'])
    db_f.duration.quarterLength = duration
    part_.append(db_f)

def silence(part_, duration = 1):

    r = note.Rest()
    r.duration.quarterLength = duration
    part_.append(r)

def eb_gChord(part_, duration = 1):

    eb_g = chord.Chord(['Eb', 'G'])
    eb_g.duration.quarterLength = duration
    part_.append(eb_g)

def f_aChord(part_, duration = 1):

    f_a = chord.Chord(['F', 'A'])
    f_a.duration.quarterLength = duration
    part_.append(f_a)

def g_bbChord(part_, duration = 1):

    g_bb = chord.Chord(['G', 'Bb'])
    g_bb.duration.quarterLength = duration
    part_.append(g_bb)

def e_gChord(part_, duration = 1):

    e_g = chord.Chord(['E', 'G'])
    e_g.duration.quarterLength = duration
    part_.append(e_g)

def d_fChord(part_, duration = 1):

    d_f = chord.Chord(['D', 'F'])
    d_f.duration.quarterLength = duration
    part_.append(d_f)

def d_gChord(part_, duration = 1):

    d_g = chord.Chord(['D', 'G'])
    d_g.duration.quarterLength = duration
    part_.append(d_g)

def c_fChord(part_, duration = 1):

    c_f = chord.Chord(['C', 'F'])
    c_f.duration.quarterLength = duration
    part_.append(c_f)

def smileChord(part_):

    a = note.Note('A')
    a.duration.quarterLength = 4

    e = note.Note('E')
    e.duration.quarterLength = 2

    d = note.Note('D')
    d.duration.quarterLength = 4

    smile = chord.Chord([a,e,d])
    part_.append(smile)

def a_cChord(part_, duration = 1):

    a_c = chord.Chord(['A3', 'C'])
    a_c.duration.quarterLength = duration
    part_.append(a_c)

def bb_dChord(part_, duration = 1):

    bb_d = chord.Chord(['Bb3', 'D'])
    bb_d.duration.quarterLength = duration
    part_.append(bb_d)

def d_bbChord(part_, duration = 1):

    d_bb = chord.Chord(['D', 'Bb'])
    d_bb.duration.quarterLength = duration
    part_.append(d_bb)

def b_fChord(part_, duration = 1):

    b_f = chord.Chord(['B3', 'F'])
    b_f.duration.quarterLength = duration
    part_.append(b_f)

def note_seq(part_):

    d = note.Note('D')
    d.duration.quarterLength = 0.5
    part_.append(d)

    d2 = note.Note('D')
    d2.duration.quarterLength = 0.75
    part_.append(d2)

    d3 = note.Note('D')
    d3.duration.quarterLength = 3
    part_.append(d3)

    r = note.Rest()
    r.duration.quarterLength = 0.25
    part_.append(r)