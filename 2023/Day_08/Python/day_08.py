"""Solution to AoC 2023 Day 8: Haunted Wasteland"""
import re
from math import lcm


def input_per_line_unique_first_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        our_input = input_file.read()
        first_line, *rest_of_lines = our_input.split("\n")
        return first_line, rest_of_lines[1:]  # get rid of space as first element


def create_map(map_nodes: list[str]) -> dict:
    """Take in the puzzle input and return a dictionary representing the connected nodes.

    dict[node] = (left_node, right_node)
    """
    map_dict = {}
    regex = re.compile(r'(\w\w\w)')
    for node in map_nodes:
        nodes = re.findall(regex, node)
        map_dict[nodes[0]] = (nodes[1], nodes[2])
    return map_dict


def get_to_zzz(node_map: dict,directions: str) -> int:
    """Traverse nodes from AAA to ZZZ. Return the number of steps required to get there."""
    directions_list = list(directions)
    completed = False
    steps = 0
    node = "AAA"
    pointer = 0
    while not completed:
        steps += 1
        direction = directions_list[pointer]
        node = node_map[node][0] if direction == "L" else node_map[node][1]
        pointer += 1
        pointer %= len(directions_list)
        if node == "ZZZ":
            return steps


def get_to_star_star_z(node_map: dict, node: str,  directions: str) -> int:
    """Simultaneously traverse nodes from **A to **Z. Return the number of steps required to get there."""
    directions_list = list(directions)
    completed = False
    steps = 0
    pointer = 0
    while not completed:
        steps += 1
        direction = directions_list[pointer]
        node = node_map[node][0] if direction == "L" else node_map[node][1]
        pointer += 1
        pointer %= len(directions_list)
        if node[-1] == "Z":
            return steps


if __name__ == '__main__':
    dirs, our_nodes = input_per_line_unique_first_line("../input.txt")
    our_map = create_map(our_nodes)
    part_two_map = create_map(our_nodes)
    part_one_steps = get_to_zzz(our_map, dirs)
    print(f"It will take {part_one_steps} steps to get to ZZZ")
    # starting part 2
    part_two_nodes = [node for node in our_map if node[-1] == "A"]
    part_two_steps = [
        get_to_star_star_z(our_map, node, dirs) for node in part_two_nodes
    ]
    least_common = lcm(*part_two_steps)
    #part_two_steps = get_to_star_star_z(our_map, dirs)
    print(f"It will take {least_common} steps to get to all the **Z nodes.")
