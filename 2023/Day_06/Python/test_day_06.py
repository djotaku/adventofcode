import day_06


def test_find_button_presses():
    assert day_06.find_button_presses(7, 9) == 4
    assert day_06.find_button_presses(15, 40) == 8
    assert day_06.find_button_presses(30, 200) == 9
