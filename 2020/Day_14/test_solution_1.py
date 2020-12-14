from . import solution_1


def test_parse_input():
    assert solution_1.parse_input('ref_input') == ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', (8, 11), (7, 101), (8, 0)]


def test_mask_application():
    assert solution_1.mask_application('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11) == 73