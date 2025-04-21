from working import convert

def test_convert():
    # Test validi
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

    # Test orario PM
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

    # Test orario non valido
    try:
        convert("12:60 AM to 5:00 PM")
    except ValueError:
        pass  # Expected ValueError
    else:
        assert False, "Expected ValueError for invalid time"

    try:
        convert("13:00 AM to 5:00 PM")
    except ValueError:
        pass  # Expected ValueError
    else:
        assert False, "Expected ValueError for invalid time"

    # Test orario in un formato sbagliato
    try:
        convert("9:00 PM 5:00 AM")
    except ValueError:
        pass  # Expected ValueError
    else:
        assert False, "Expected ValueError for invalid format"

