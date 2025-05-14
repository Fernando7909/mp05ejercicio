from strings import majuscules, minuscules

def test_majuscules():
    assert majuscules ("abcdefg") == "ABCDEFG"
    assert majuscules("aBcDeFG") == "ABCDEFG"

def test_minuscules():
    assert minuscules ("ABCDEFG") == "abcdefg"
    assert minuscules("AbCdEfG") == "abcdefg"