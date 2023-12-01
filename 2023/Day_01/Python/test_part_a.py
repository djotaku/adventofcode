import day_01


def test_find_numbers():
    assert day_01.find_numbers("1abc2") == ["1", "2"]
    assert day_01.find_numbers("pqr3stu8vwx") == ["3", "8"]
    assert day_01.find_numbers("a1b2c3d4e5f") == ["1", "2", "3", "4", "5"]
    assert day_01.find_numbers("treb7uchet") == ["7"]


def test_create_number():
    assert day_01.create_number(day_01.find_numbers("1abc2")) == 12
    assert day_01.create_number(day_01.find_numbers("pqr3stu8vwx")) == 38
    assert day_01.create_number(day_01.find_numbers("a1b2c3d4e5f")) == 15
    assert day_01.create_number(day_01.find_numbers("treb7uchet")) == 77


def test_find_numbers_part_2():
    assert day_01.find_numbers_part_2("two1nine") == ["2", "1", "9"]
    assert day_01.find_numbers_part_2("eightwothree") == ["8", "2", "3"]

