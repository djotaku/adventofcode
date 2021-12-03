from . import solution

sample = ["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]


def test_oxygen_generator():
    assert solution.generator_ratings(sample, "o2", 0) == 23


def test_carbon_dioxide_generator():
    assert solution.generator_ratings(sample, "co2", 0) == 10