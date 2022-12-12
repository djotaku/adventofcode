""" Solution to Aoc 2016 Day 23 - Safe Cracking"""
import math

"""Solution to Advent of Code 2016 Day 12: Leonardo's Monorail."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def run_bunny_assembly(registers: dict, part_two=False) -> dict:
    """
    Runs bunny assembly based on initial registers.

    Returns registers at the end.
    """
    counter = 0
    while counter < len(our_input):
        # print(f"{our_input=}")
        components = our_input[counter].split()
        instruction = components[0]
        # print(components)
        x = components[1]
        y = 0
        if len(components) == 3:
            y = components[2]
        match instruction:
            case "cpy":  # copies x (either an integer or the value of a register) into register y
                if isinstance(y, int):
                    break
                if x == "a" or x == "b" or x == "c" or x == "d":
                    registers[y] = int(registers[x])
                else:
                    registers[y] = int(x)
                counter += 1
            case "inc":  # increases the value of register x by one
                registers[x] += 1
                counter += 1
            case "dec":  # decreases the value of register x by one
                registers[x] -= 1
                counter += 1
            case "jnz":  # jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
                jump_location = 0
                if y in ["a", "b", "c", "d"]:
                    jump_location = registers[y]
                else:
                    jump_location = int(y)
                if x in ["a", "b", "c", "d"]:
                    if registers[x] != 0:
                        counter += jump_location
                    else:
                        counter += 1
                else:
                    if x != 0:
                        counter += jump_location
                    else:
                        counter += 1
            # need to add in the tgl instruction
            # need a try/catch in case it tries to modify a spot outside the list
            case "tgl":
                distance = 0
                if x in ["a", "b", "c", "d"]:
                    distance = registers[x]
                else:
                    distance = int(x)
                try:
                    modified_command = toggle_transform(our_input[counter + distance])
                    our_input[counter + distance] = modified_command
                except:
                    print("tried to go beyond the list")
                counter += 1
        # print(registers)
    return registers


def toggle_transform(assembly: str) -> str:
    """Take in assembly code and transform it based on toggle rules. Return the new string."""
    split = assembly.split()
    if len(split) == 2:
        if split[0] == "inc":
            split[0] = "dec"
        else:
            split[0] = "inc"
    elif len(split) == 3:
        if split[0] == "jnz":
            split[0] = "cpy"
        else:
            split[0] = "jnz"
    return " ".join(split)

if __name__ == "__main__":
    our_input = input_per_line('../input.txt')
    part_1_initial_registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    part_1_final_registers = run_bunny_assembly(part_1_initial_registers)
    print("Part 1:")
    print(f"{part_1_final_registers=}")
    print("Part 2")
    print("It's a joke revolving around factorial and bunnies multiplying")
    constant = 85 * 76
    bunny_factorial = math.factorial(12)
    print(f"Part 2 answer is {bunny_factorial + constant}")

# 6592 iw too low - but I hadn't changed to multiplicatoin yet.