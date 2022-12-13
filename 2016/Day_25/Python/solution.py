""" Solution to Aoc 2016 Day 25- Clock Signal"""
import math


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def run_bunny_assembly(registers: dict) -> list:
    """
    Runs bunny assembly based on initial registers.

    Returns output at the end.
    """
    counter = 0
    output = []
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
                registers[y] = int(registers[x]) if x in ["a", "b", "c", "d"] else int(x)
                counter += 1
            case "inc":  # increases the value of register x by one
                registers[x] += 1
                counter += 1
            case "dec":  # decreases the value of register x by one
                registers[x] -= 1
                counter += 1
            case "jnz":  # jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
                jump_location = registers[y] if y in ["a", "b", "c", "d"] else int(y)
                if x in ["a", "b", "c", "d"] and registers[x] != 0 or x not in ["a", "b", "c", "d"] and int(x) != 0:
                    counter += jump_location
                else:
                    counter += 1
            case "tgl":
                distance = registers[x] if x in ["a", "b", "c", "d"] else int(x)
                try:
                    modified_command = toggle_transform(our_input[counter + distance])
                    our_input[counter + distance] = modified_command
                except Exception:
                    print("tried to go beyond the list")
                counter += 1
            case "out":
                if x in ["a", "b", "c", "d"]:
                    output.append(registers[x])
                else:
                    output.append(x)

        if len(output) == 20:
            return output
    return output


def toggle_transform(assembly: str) -> str:
    """Take in assembly code and transform it based on toggle rules. Return the new string."""
    split = assembly.split()
    if len(split) == 2:
        split[0] = "dec" if split[0] == "inc" else "inc"
    elif len(split) == 3:
        split[0] = "cpy" if split[0] == "jnz" else "jnz"
    return " ".join(split)


if __name__ == "__main__":
    our_input = input_per_line('../input.txt')
    output_signals = []
    for a in range(10000):
        print(a)
        # print(f"we're trying {a=}")
        part_1_initial_registers = {"a": a, "b": 0, "c": 0, "d": 0}
        output_signals = run_bunny_assembly(part_1_initial_registers)
        # print(f"testing output: {output_signals}")
        if output_signals[0] == 0 and output_signals[1] == 1 and output_signals[2] == 0 and output_signals[3] == 1:
            print(output_signals)
            print(f"{a=}")
            break
    print("And we're done.")
