from main import convert_date, masking_card

def test_convert_date():
    assert convert_date("2019-08-26T23:20:15.28564") == "26.08.2019"
    assert convert_date("2019-03-23T23:20:15.28564") == "23.03.2019"

def test_masking_card():
    assert masking_card("Счет 97848259954268659635") == "Счет **9635"
    assert masking_card("Maestro 1596837868705199") == "Maestro 1596 83** ***** 5199"