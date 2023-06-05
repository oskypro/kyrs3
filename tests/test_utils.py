import pytest



assert test_convert_date("2019-03-23T23:20:15.28564") == "23.03.2019"


def test_convert_date():
    assert test_convert_date("2019-04-08T23:20:15.28564") == "08.04.2019"
    assert test_convert_date("2019-03-23T23:20:15.28564") == "23.03.2019"


def test_masking_card():
    assert masking_card("Счет 35158586384610753655") == "Счет ** 3655"
    assert masking_card("Visa Classic 2842878893689012") == "Visa Classic ** 9012"



