"""Solution for Advent of Code 2021 Day 24: Arithmetic Logic Unit"""
from math import floor


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def math(a, b, this_instruction):
    print(f"Doing math. Param {a=}. Param {b=} with {this_instruction=}")
    if this_instruction == 'add':
        return int(a) + int(b)
    elif this_instruction == "mul":
        return int(a) * int(b)
    elif this_instruction == "div":
        return floor(int(a)/int(b))
    elif this_instruction == "mod":
        return int(a) % int(b)
    elif this_instruction == "eql":
        if int(a) == int(b):
            return 1
        else:
            return 0


if __name__ == "__main__":
    instructions = input_per_line("../input.txt")
    # initialize registers
    w, x, y, z = 0, 0, 0, 0
    letter_dict = {"w": w, "x": x, "y": y, "z": z}
    inp_counter = 0
    test_number = 99999999999999
    add_2 = 0
    test_number_as_list = [int(x) for x in str(test_number)]
    # print(f"{len(test_number_as_list)=}")
    while True:
        # print(f"{test_number=} at beginning")
        # print(f"{test_number_as_list=}")
        for instruction in instructions:
            parsed_instruction = instruction.split()
            print(f"{parsed_instruction=}")
            if len(parsed_instruction) == 2:
                if parsed_instruction[0] == "inp":
                    if parsed_instruction[1] == "w":
                        w = test_number_as_list[inp_counter]
                        inp_counter += 1
            else:
                if parsed_instruction[2] in ["w", "x", "y", "z"]:
                    if parsed_instruction[2] == "w":
                        add_2 = w
                    elif parsed_instruction[2] == "x":
                        add_2 = x
                    elif parsed_instruction[2] == "y":
                        add_2 = y
                    elif parsed_instruction[2] == "z":
                        add_2 = z
                else:
                    add_2 = int(parsed_instruction[2])
                if parsed_instruction[1] == "w":
                    w = math(w, add_2, parsed_instruction[0])
                elif parsed_instruction[1] == "x":
                    x = math(x, add_2, parsed_instruction[0])
                elif parsed_instruction[1] == "y":
                    y = math(y, add_2, parsed_instruction[0])
                elif parsed_instruction[1] == "z":
                    z = math(z, add_2, parsed_instruction[0])
                print(f"{w=}, {x=}, {y=}, {z=}")
        if z == 0:
            break
        test_number -= 1
        print(f"{test_number=} at end")
        test_number_as_list = [int(x) for x in str(test_number)]
        inp_counter = 0
        if 0 in test_number_as_list:
            test_number -= 1
            test_number_as_list = [int(x) for x in str(test_number)]
        w, x, y, z = 0, 0, 0, 0
    print(f"The model number is {test_number}")


# answer is not 99999999999999 so need to check algorithm
