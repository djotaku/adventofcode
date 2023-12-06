import day_05


# def test_generate_map():
#     seed_to_soil = ["50 98 2", "52 50 48"]
#     test_map = day_05.generate_map(seed_to_soil)
#     assert test_map[98] == 50
#     assert test_map[99] == 51


def test_generate_map():
    seed_to_soil = ["50 98 2", "52 50 48"]
    test_map = day_05.generate_map(seed_to_soil)
    assert test_map[0].source_begin == 98

def test_correct_value_found():
    seed_row, mappings = day_05.input_per_line_unique_first_line("../sample_input.txt")
    day_05.fill_in_map_of_maps(mappings)
    assert day_05.map_conversion(79, "seed-to-soil") == 81


def test_sample_input_final_answer():
    seed_row, mappings = day_05.input_per_line_unique_first_line("../sample_input.txt")
    day_05.fill_in_map_of_maps(mappings)
    seeds = day_05.get_seeds(seed_row)
    seed_locations = [day_05.find_location(seed) for seed in seeds]
    assert min(seed_locations) == 35


def test_get_seeds():
    seed_line = "seeds: 79 14 55 13"
    assert day_05.get_seeds(seed_line) == [79, 14, 55, 13]

