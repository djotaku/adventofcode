"""Solution to AoC 2023 Day 5: If You Give A Seed A Fertilizer"""
import re

map_of_maps = {}


def input_per_line_unique_first_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        our_input = input_file.read()
        first_line, *rest_of_lines = our_input.split("\n")
        return first_line, rest_of_lines[1:]  # get rid of space as first element


def generate_map(map_info: list[str]) -> dict:
    """Given a list of strings with mapping info, make the map, ie dict, and return it.

    The numbers are in the order destination source range.

    In other words:

    50 98 2 means that key of 98 gives 50 and key of 99 gives value of 51.
    """
    destination_list = []
    source_list = []
    for line in map_info:
        destination, source, map_range = line.split()
        destination = int(destination)
        source = int(source)
        map_range = int(map_range)
        while map_range > 0:
            destination_list.append(destination)
            source_list.append(source)
            destination += 1
            source += 1
            map_range -= 1
    return {
        source_item: destination_list[pos]
        for pos, source_item in enumerate(source_list)
    }


def fill_in_map_of_maps(mappings: list[str]):
    """Go through all the mappings and fill out the main dictionary."""
    the_key = ""
    the_numbers = []
    for the_map in mappings:
        if "-" in the_map:
            the_key, _ = the_map.split()
        elif the_map != "":
            the_numbers.append(the_map)
        elif the_map == "":
            map_of_maps[the_key] = generate_map(the_numbers.copy())
            the_key = ""
            the_numbers.clear()
    # final entry
    map_of_maps[the_key] = generate_map(the_numbers)


def get_seeds(seed_line: str) -> list[int]:
    """Given the seed line, extract the seeds."""
    regex = re.compile(r'(\d+)')
    numbers = re.findall(regex, seed_line)
    return [int(number) for number in numbers]


def find_location(seed: int) -> int:
    soil_location = map_of_maps["seed-to-soil"].get(seed)
    if soil_location is None:
        soil_location = seed
    # print(f"{soil_location=}")
    fertilizer_location = map_of_maps["soil-to-fertilizer"].get(soil_location)
    if fertilizer_location is None:
        fertilizer_location = soil_location
    # print(f"{fertilizer_location=}")
    water_location = map_of_maps["fertilizer-to-water"].get(fertilizer_location)
    if water_location is None:
        water_location = fertilizer_location
    # print(f"{water_location=}")
    light_location = map_of_maps["water-to-light"].get(water_location)
    if light_location is None:
        light_location = water_location
    # print(f"{light_location=}")
    temperature_location = map_of_maps["light-to-temperature"].get(light_location)
    if temperature_location is None:
        temperature_location = light_location
    # print(f"{temperature_location=}")
    humidity_location = map_of_maps["temperature-to-humidity"].get(temperature_location)
    if humidity_location is None:
        humidity_location = temperature_location
    location_location = map_of_maps["humidity-to-location"].get(humidity_location)
    if location_location is None:
        location_location = humidity_location
    return location_location


if __name__ == '__main__':
    seed_row, mappings = input_per_line_unique_first_line("../sample_input.txt")
    print("filling in map")
    fill_in_map_of_maps(mappings)
    print(mappings)
    # print(map_of_maps["humidity-to-location"])
    print("getting seeds")
    seeds = get_seeds(seed_row)
    seed_locations = [find_location(seed) for seed in seeds]
    print(f"The lowest location is {min(seed_locations)}")
