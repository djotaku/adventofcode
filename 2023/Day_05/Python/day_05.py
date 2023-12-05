"""Solution to AoC 2023 Day 5: If You Give A Seed A Fertilizer"""

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