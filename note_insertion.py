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
    r.duration.quarterLength = 3.5
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

    d = note.Note('D')
    d.duration.quarterLength = 0.5
    d.insertLyric('And')
    part_.append(d)

def m021(part_):

    d = note.Note('D')
    d.duration.quarterLength = 0.5
    d.insertLyric('with')
    part_.append(d)

    bflat = note.Note('Bb')
    bflat.duration.quarterLength = 1.5
    bflat.insertLyric('out')
    part_.append(bflat)

    bflat2 = note.Note('Bb')
    bflat2.duration.quarterLength = 0.5
    bflat2.insertLyric('real')
    part_.append(bflat2)

    a = note.Note('A')
    a.duration.quarterLength = 1.5
    a.insertLyric('ly')
    part_.append(a)

def m022(part_):

    a = note.Note('A')
    a.duration.quarterLength = 0.5
    a.insertLyric('en')
    part_.append(a)

    g = note.Note('G')
    g.duration.quarterLength = 0.5
    g.insertLyric('ter')
    part_.append(g)

    g2 = note.Note('G')
    g2.duration.quarterLength = 2
    g2.insertLyric('ing')
    part_.append(g2)

    c = note.Note('C')
    c.duration.quarterLength = 0.5
    c.insertLyric('her')
    part_.append(c)

    c2 = note.Note('C')
    c2.duration.quarterLength = 1.5
    c2.insertLyric('world')
    part_.append(c2)

def m023(part_):

    r = note.Rest()
    r.duration.quarterLength = 3
    part_.append(r)

def m024(part_):

    r = note.Rest()
    r.duration.quarterLength = 3
    part_.append(r)

    c = note.Note('C')
    c.insertLyric("I'm")
    part_.append(c)

def m025(part_):

    d = note.Note('D')
    d.insertLyric('glad')
    part_.append(d)

    bflat = note.Note('Bb')
    bflat.insertLyric('when')
    part_.append(bflat)

    bflat2 = note.Note('Bb')
    bflat2.duration.quarterLength = 0.5
    bflat2.insertLyric('ev')
    part_.append(bflat2)

    a = note.Note('A')
    a.insertLyric('er')
    part_.append(a)

    a2 = note.Note('A')
    a2.insertLyric('I')
    part_.append(a2)

def m026(part_):

    g = note.Note('G')
    g.duration.quarterLength = 1.5
    g.insertLyric('can')
    part_.append(g)

    g2 = note.Note('G')
    g2.insertLyric('share')
    part_.append(g2)

    c = note.Note('C')
    c.duration.quarterLength = 0.5
    c.insertLyric('her')
    part_.append(c)

    c2 = note.Note('C')
    c2.insertLyric('laugh')
    part_.append(c2)

def m027(part_):

    a = note.Note('A')
    a.duration.quarterLength = 0.5
    part_.append(a)

    a2 = note.Note('A')
    a2.insertLyric('ter')
    part_.append(a2)

    r = note.Rest()
    part_.append(r)

    c = note.Note('C')
    c.insertLyric('That')
    part_.append(c)

def m028(part_):

    c = note.Note('C')
    c.duration.quarterLength = 0.5
    c.insertLyric('fun')
    part_.append(c)

    g = note.Note('G')
    g.duration.quarterLength = 1.5
    g.insertLyric('ny')
    part_.append(g)

    g2 = note.Note('G')
    g2.duration.quarterLength = 0.5
    g2.insertLyric('lit')
    part_.append(g2)

    f = note.Note('F')
    f.insertLyric('tle')
    part_.append(f)

    f2 = note.Note('F')
    f2.duration.quarterLength = 2.5
    f2.insertLyric('girl')
    part_.append(f2)

def m029(part_):

    r = note.Rest()
    r.duration.quarterLength = 2
    part_.append(r)

def m030(part_):

    r = note.Rest()
    r.duration.quarterLength = 2
    part_.append(r)

    a = note.Note('A3')
    a.duration.quarterLength = 0.5
    a.insertLyric('Slip')
    part_.append(a)

    c = note.Note('C')
    c.duration.quarterLength = 0.5
    c.insertLyric('ping')
    part_.append(c)

    f = note.Note('F')
    f.duration.quarterLength = 0.5
    f.insertLyric('through')
    part_.append(f)

    a2 = note.Note('A')
    a2.duration.quarterLength = 0.5
    a2.insertLyric('my')
    part_.append(a2)

def m031(part_):

    a = note.Note('A')
    a.duration.quarterLength = 0.5
    a.insertLyric('fin')
    part_.append(a)

    g = note.Note('G')
    g.duration.quarterLength = 1.5
    g.insertLyric('gers')
    part_.append(g)

    g2 = note.Note('G')
    g2.insertLyric('all')
    part_.append(g2)

    f = note.Note('F')
    f.duration.quarterLength = 0.5
    f.insertLyric('the')
    part_.append(f)

    f2 = note.Note('F')
    f2.duration.quarterLength = 1.5
    f2.insertLyric('time')
    part_.append(f2)

def m032(part_):

    c = note.Note('C5')
    c.insertLyric('I')
    part_.append(c)

    a = note.Note('A')
    a.insertLyric('try')
    part_.append(a)

    f = note.Note('F')
    f.duration.quarterLength = 0.5
    f.insertLyric('to')
    part_.append(f)

    e = note.Note('E')
    e.duration.quarterLength = 1.5
    e.insertLyric('cap')
    part_.append(e)

def m033(part_):

    c = note.Note('C5')
    c.insertLyric('ture')
    part_.append(c)

    a = note.Note('A')
    a.insertLyric('ev')
    part_.append(a)

    e = note.Note('E')
    e.duration.quarterLength = 0.5
    e.insertLyric("'ry")
    part_.append(e)

    d = note.Note('D')
    d.insertLyric('min')
    part_.append(d)

def m034(part_):

    g = note.Note('G')
    g.duration.quarterLength = 2.5
    g.insertLyric('ute,')
    part_.append(g)

    r = note.Rest()
    part_.append(r)

def m035(part_):

    r = note.Rest()
    part_.append(r)

    g = note.Note('G')
    g.duration.quarterLength = 0.5
    g.insertLyric('the')
    part_.append(g)

    r2 = note.Rest()
    r2.duration.quarterLength = 0.5
    part_.append(r2)

    f = note.Note('F')
    f.insertLyric('feel')
    part_.append(f)

    d = note.Note('D')
    d.duration.quarterLength = 0.5
    d.insertLyric('ing')
    part_.append(d)

    c = note.Note('C')
    c.insertLyric('in')
    part_.append(c)

def m036(part_):

    f = note.Note('F')
    f.insertLyric('it')
    part_.append(f)

    r = note.Rest()
    r.duration.quarterLength = 0.5
    part_.append(r)

    a = note.Note('A3')
    a.duration.quarterLength = 0.5
    a.insertLyric('Slip')
    part_.append(a)

    c = note.Note('C')
    c.duration.quarterLength = 0.5
    c.insertLyric('ping')
    part_.append(c)

    f2 = note.Note('F')
    f2.duration.quarterLength = 0.5
    f2.insertLyric('through')
    part_.append(f2)

    a2 = note.Note('A')
    a2.duration.quarterLength = 0.5
    a2.insertLyric('my')
    part_.append(a2)