from plates import is_valid

def test_min_2_max_6():
    assert is_valid("altifdi") == False

def test_a_z():
    assert is_valid("5050") == False

def test_caratteri_speciali():
    assert is_valid("alt$fi") == False

def test_la_sequenza_di_numeri_della_parola_non_puo_iniziare_con_0():
    assert is_valid("alti02") == False

def test_numeri_in_mezzo_alla_parola():
    assert is_valid("al23fi") == False
