import day_05


def test_generate_map():
    seed_to_soil = ["50 98 2", "52 50 48"]
    test_map = day_05.generate_map(seed_to_soil)
    assert test_map[98] == 50
    assert test_map[99] == 51


def test_get_seeds():
    seed_line = "seeds: 79 14 55 13"
    assert day_05.get_seeds(seed_line) == [79, 14, 55, 13]

