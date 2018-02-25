import songcalc.songcalc as sc


def test_zipf():
    assert sc.SongCalc.zipf(1) == 1.0


def test_zipf_div_by_zero():
    assert sc.SongCalc.zipf(0) is None


def test_quality():
    assert sc.SongCalc.quality(50, 5) == 10.0


def test_quality_div_by_zero():
    assert sc.SongCalc.quality(50, 0) is None


def test_get_songdata():
    lines = sc.SongCalc.get_songdata('album1.dat')
    assert lines[0][0][0] == 6
    assert lines[0][0][1] == '2000'
    assert lines[0][0][2] == 'six'
