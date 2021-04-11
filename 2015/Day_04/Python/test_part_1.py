from . import part_1


def test_calculate_hash():
    assert part_1.calculate_hash("abcdef609043") == "000001dbbfa3a5c83a2d506429c7b00e"


def test_does_it_lead():
    assert part_1.does_it_lead_with_five_zeroes("000001dbbfa3a5c83a2d506429c7b00e") is True
    assert part_1.does_it_lead_with_five_zeroes("00001dbbfa3a5c83a2d506429c7b00e") is False


def test_find_special_number():
    assert part_1.find_special_number("abcdef") == 609043
    assert part_1.find_special_number("pqrstuv") == 1048970

