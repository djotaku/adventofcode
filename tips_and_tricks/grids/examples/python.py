def text_to_grid(text_map: list) -> (dict, int, int):
    """Take in a list of items that need to be parsed into a dictionary where each set of keys is a coordinate.

    Return a dictionary representation of the map.
    """
    grid_map = defaultdict(int)
    max_y = len(text_map)
    max_x = len(text_map[0])
    for y, line in enumerate(text_map):
        for x, number in enumerate(line):
            grid_map[(x, y)] = int(number)
    return grid_map, max_x, max_y