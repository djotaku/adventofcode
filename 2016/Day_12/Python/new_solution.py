"""Solution to Advent of Code 2016 Day 12: Leonardo's Monorail."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def run_bunny_assembly(registers: dict) -> dict:
    """
    Runs bunny assembly based on initial registers.

    Returns registers at the end.
    """
    counter = 0
    while counter < len(our_input):
        components = our_input[counter].split()
        instruction = components[0]
        x = components[1]
        y = 0
        if len(components) == 3:
            y = components[2]
        match instruction:
            case "cpy":
                if x == "a" or x == "b" or x == "c" or x == "d":
                    registers[y] = int(registers[x])
                else:
                    registers[y] = int(x)
                counter += 1
            case "inc":
                registers[x] += 1
                counter += 1
            case "dec":
                registers[x] -= 1
                counter += 1
            case "jnz":
                if x in ["a", "b", "c", "d"]:
                    if registers[x] != 0:
                        counter += int(y)
                    else:
                        counter += 1
                else:
                    if x != 0:
                        counter += int(y)
                    else:
                        counter += 1
    return registers

if __name__ == "__main__":
    our_input = input_per_line('../input.txt')
    part_1_initial_registers = {"a": 0, "b":0, "c":0, "d":0}
    part_1_final_registers = run_bunny_assembly(part_1_initial_registers)
    print("Part 1:")
    print(f"{part_1_final_registers=}")
    part_2_initial_registers = {"a": 0, "b":0, "c":1, "d":0}
    part_2_final_registers = run_bunny_assembly(part_2_initial_registers)
    print("Part 2:")
    print(f"{part_2_final_registers=}")
