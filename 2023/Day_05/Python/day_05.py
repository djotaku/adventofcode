"""Solution to AoC 2023 Day 5: If You Give A Seed A Fertilizer"""
import re
from collections import namedtuple

map_of_maps = {}

Mapping = namedtuple("Mapping", ["source_begin", "source_end", "destination_begin", "destination_end"])


def input_per_line_unique_first_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        our_input = input_file.read()
        first_line, *rest_of_lines = our_input.split("\n")
        return first_line, rest_of_lines[1:]  # get rid of space as first element


def generate_map(map_info: list[str]) -> list:
    """Given a list of strings with mapping info, make the map, ie dict, and return it.

    The numbers are in the order destination source range.

    In other words:

    50 98 2 means that key of 98 gives 50 and key of 99 gives value of 51.
    """
    maps = []
    for line in map_info:
        destination, source, map_range = line.split()
        destination = int(destination)
        source = int(source)
        map_range = int(map_range)
        maps.append(Mapping(source_begin=source, source_end=source + map_range,
                            destination_begin=destination, destination_end=destination + map_range))
    return maps


def fill_in_map_of_maps(mappings: list[str]):
    """Go through all the mappings and fill out the main dictionary."""
    the_key = ""
    the_numbers = []
    for the_map in mappings:
        if "-" in the_map:
            the_key, _ = the_map.split()
        elif the_map != "":
            the_numbers.append(the_map)
        else:
            map_of_maps[the_key] = generate_map(the_numbers)
            the_key = ""
            the_numbers.clear()
    # final entry
    map_of_maps[the_key] = generate_map(the_numbers)


def get_seeds(seed_line: str) -> list[int]:
    """Given the seed line, extract the seeds."""
    regex = re.compile(r'(\d+)')
    numbers = re.findall(regex, seed_line)
    return [int(number) for number in numbers]


def map_conversion(number: int, dict_key: str) -> int | None:
    final_destination = None
    maps = map_of_maps[dict_key]
    return next(
        (
            this_map.destination_begin + (number - this_map.source_begin)
            for this_map in maps
            if this_map.source_begin <= number < this_map.source_end
        ),
        None,
    )


def find_location(seed: int) -> int:
    soil_location = map_conversion(seed, "seed-to-soil")
    if soil_location is None:
        soil_location = seed
    fertilizer_location = map_conversion(soil_location, "soil-to-fertilizer")
    if fertilizer_location is None:
        fertilizer_location = soil_location
    water_location = map_conversion(fertilizer_location, "fertilizer-to-water")
    if water_location is None:
        water_location = fertilizer_location
    light_location = map_conversion(water_location, "water-to-light")
    if light_location is None:
        light_location = water_location
    temperature_location = map_conversion(light_location, "light-to-temperature")
    if temperature_location is None:
        temperature_location = light_location
    humidity_location = map_conversion(temperature_location, "temperature-to-humidity")
    if humidity_location is None:
        humidity_location = temperature_location
    location_location = map_conversion(humidity_location, "humidity-to-location")
    if location_location is None:
        location_location = humidity_location
    return location_location


if __name__ == '__main__':
    seed_row, mappings = input_per_line_unique_first_line("../input.txt")
    fill_in_map_of_maps(mappings)
    seeds = get_seeds(seed_row)
    seed_locations = [find_location(seed) for seed in seeds]
    print(f"The lowest location is {min(seed_locations)}")
