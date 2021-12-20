"""Test solution to Advent of Code 2021 Day 20: Trench Map"""
from . import solution


def test_create_initial_map():
    translation, image = solution.input_per_line_unique_first_line("../sample_input.txt")
    this_map, _ = solution.create_initial_map(image)
    assert sum(this_map.values()) == 10


def test_enhance_image():
    translation, image = solution.input_per_line_unique_first_line("../sample_input.txt")
    this_map, coordinates = solution.create_initial_map(image)
    translation = [character for character in translation]
    new_map, new_coordinates = solution.enhance_image(translation, this_map, coordinates[0], coordinates[1])
    _, transform_one_image = solution.input_per_line_unique_first_line("../sample_input_transform_one.txt")
    transform_one_map, _ = solution.create_initial_map(transform_one_image)
    assert sum(new_map.values()) == sum(transform_one_map.values())


def test_enhance_image_twice():
    translation, image = solution.input_per_line_unique_first_line("../sample_input.txt")
    this_map, coordinates = solution.create_initial_map(image)
    translation = [character for character in translation]
    new_map, new_coordinates = solution.enhance_image(translation, this_map, coordinates[0], coordinates[1])
    _, transform_one_image = solution.input_per_line_unique_first_line("../sample_input_transform_one.txt")
    transform_one_map, _ = solution.create_initial_map(transform_one_image)
    _, transform_two_image = solution.input_per_line_unique_first_line("../sample_input_transform_two.txt")
    transform_two_map, _ = solution.create_initial_map(transform_two_image)
    second_enhancement_map, newest_coordinates = solution.enhance_image(translation,
                                                                        new_map,
                                                                        new_coordinates[0], new_coordinates[1])
    assert sum(second_enhancement_map.values()) == sum(transform_two_map.values())
