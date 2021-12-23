"""Solution for Advent of Code 2021 Day 22: Reactor Reboot"""
from collections import namedtuple
import re

instruction_tuple = namedtuple("Instruction", ["on_or_off", "x_min", "x_max", "y_min", "y_max", "z_min", "z_max"])


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def parse_instruction(instruction: str):
    """Take in an instruction and return a named tuple with the parameters."""
    on_off, x_y_z = instruction.split()
    x, y, z = x_y_z.split(",")
    regex = re.compile(r'\w=(-*\d+)..(-*\d+)')
    x_min_max = re.findall(regex, x)
    y_min_max = re.findall(regex, y)
    z_min_max = re.findall(regex, z)
    return instruction_tuple(on_or_off=on_off,
                             x_min=int(x_min_max[0][0]), x_max=int(x_min_max[0][1]),
                             y_min=int(y_min_max[0][0]), y_max=int(y_min_max[0][1]),
                             z_min=int(z_min_max[0][0]), z_max=int(z_min_max[0][1]))


def initialize_cuboid(instruction, current_cubes: dict) -> dict:
    """Take in instruction tuple and return dictionary with the modified cores."""
    for x in range(instruction.x_min, instruction.x_max+1):
        for y in range(instruction.y_min, instruction.y_max+1):
            for z in range(instruction.z_min, instruction.z_max+1):
                if instruction.on_or_off == "on":
                    current_cubes[(x, y, z)] = 1
                elif instruction.on_or_off == "off":
                    current_cubes[(x, y, z)] = 0
    return current_cubes


def initialize_cuboid_sets(instruction, current_cubes: dict) -> dict:
    """Take in instruction tuple and return dictionary with the modified cores."""
    for x in range(instruction.x_min, instruction.x_max+1):
        for y in range(instruction.y_min, instruction.y_max+1):
            for z in range(instruction.z_min, instruction.z_max+1):
                if instruction.on_or_off == "on":
                    current_cubes[(x, y, z)] = 1
                    # current_cubes.add((x, y, z))
                elif instruction.on_or_off == "off":
                    current_cubes[(x, y, z)] = 0
                    try:
                        pass
                        # current_cubes.remove((x, y, z))
                    except KeyError:
                        pass
    return current_cubes


def cubes_in_part_one(cubes_at_end: dict) -> int:
    """Sum up the turned on cubes in -50-50 cuboid."""
    return sum(cubes_at_end.get((x, y, z), 0) for x in range(-50, 50)
               for y in range(-50, 50)
               for z in range(-50, 50))


if __name__ == "__main__":
    our_instructions = input_per_line("../larger_sample_input.txt")
    cubes = set()
    for the_instruction in our_instructions:
        this_instruction = parse_instruction(the_instruction)
        cubes = initialize_cuboid(this_instruction, cubes)
    part_one_answer = cubes_in_part_one(cubes)
    print(f"There are {part_one_answer} cubes lit.")
