from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("h") == 20

def test_other():
    assert value("") == 100

def test_case_insensitivity():
    assert value("HELLO") == 0

def test_case_entire_phrase():
    assert value("HELLO boy") == 0
