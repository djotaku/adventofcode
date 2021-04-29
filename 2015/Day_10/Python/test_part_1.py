from . import part_1


def test_create_number_lists():
    assert part_1.create_number_lists("1") == (['1'])
    assert part_1.create_number_lists("11") == (['1', '1'])
