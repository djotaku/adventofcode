import day_08


def test_get_to_zzz():
    first_line, rest = day_08.input_per_line_unique_first_line("../sample_input_1.txt")
    map_dict = day_08.create_map(rest)
    steps = day_08.get_to_zzz(map_dict, first_line)
    assert steps == 2
    first_line, rest = day_08.input_per_line_unique_first_line("../sample_input_2.txt")
    map_dict = day_08.create_map(rest)
    steps = day_08.get_to_zzz(map_dict, first_line)
    assert steps == 6