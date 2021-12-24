"""Solution for Advent of Code 2021 Day 24: Arithmetic Logic Unit"""
from math import floor


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


if __name__ == "__main__":
    instructions = input_per_line("../input.txt")
    # initialize registers
    w, x, y, z = 0, 0, 0, 0
    inp_counter = 0
    test_number = 99999999999999
    test_number_as_list = [int(x) for x in str(test_number)]
    while True:
        for instruction in instructions:
            parsed_instruction = instruction.split()
            # print(parsed_instruction)
            match parsed_instruction[0]:
                case "inp":
                    value_to_store = test_number_as_list[inp_counter]
                    inp_counter += 1
                    # print(f"{inp_counter=}")
                    match parsed_instruction[1]:
                        case "w":
                            # print(f"case is w and it should get {value_to_store}")
                            w = int(value_to_store)
                        case "x":
                            x = int(value_to_store)
                        case "y":
                            y = int(value_to_store)
                        case "z":
                            z = int(value_to_store)
                case "add":
                    add_1 = 0
                    add_2 = 0
                    match parsed_instruction[2]:
                        case "w":
                            add_2 = w
                        case "x":
                            add_2 = x
                        case "y":
                            add_2 = y
                        case "z":
                            add_2 = z
                        case _:
                            add_2 = int(parsed_instruction[2])
                    match parsed_instruction[1]:
                        case "w":
                            w = w + int(add_2)
                        case "x":
                            x = x + int(add_2)
                        case "y":
                            y = y + int(add_2)
                        case "z":
                            z = z + int(add_2)
                case "mul":
                    match parsed_instruction[2]:
                        case "w":
                            mul_2 = w
                        case "x":
                            mul_2 = x
                        case "y":
                            mul_2 = y
                        case "z":
                            mul_2 = z
                        case _:
                            mul_2 = int(parsed_instruction[2])
                    match parsed_instruction[1]:
                        case "w":
                            mul_1 = w
                            w = int(mul_1) * int(mul_2)
                        case "x":
                            mul_1 = x
                            x = int(mul_1) * int(mul_2)
                        case "y":
                            mul_1 = y
                            y = int(mul_1) * int(mul_2)
                        case "z":
                            mul_1 = z
                            z = int(mul_1) * int(mul_2)
                case "div":
                    match parsed_instruction[2]:
                        case "w":
                            div_2 = w
                        case "x":
                            div_2 = x
                        case "y":
                            div_2 = y
                        case "z":
                            div_2 = z
                        case _:
                            div_2 = int(parsed_instruction[2])
                    match parsed_instruction[1]:
                        case "w":
                            div_1 = w
                            w = floor(int(div_1)/int(div_2))
                        case "x":
                            div_1 = x
                            x = floor(int(div_1)/int(div_2))
                        case "y":
                            div_1 = y
                            y = floor(int(div_1)/int(div_2))
                        case "z":
                            div_1 = z
                            z = floor(int(div_1)/int(div_2))
                case "mod":
                    match parsed_instruction[2]:
                        case "w":
                            mod_2 = w
                        case "x":
                            mod_2 = x
                        case "y":
                            mod_2 = y
                        case "z":
                            mod_2 = z
                        case _:
                            mod_2 = int(parsed_instruction[2])
                    match parsed_instruction[1]:
                        case "w":
                            mod_1 = w
                            w = int(mod_1) % int(mod_2)
                        case "x":
                            mod_1 = x
                            x = int(mod_1) % int(mod_2)
                        case "y":
                            mod_1 = y
                            y = int(mod_1) % int(mod_2)
                        case "z":
                            mod_1 = z
                            z = int(mod_1) % int(mod_2)
                case "eql":
                    match parsed_instruction[2]:
                        case "w":
                            eql_2 = w
                        case "x":
                            eql_2 = x
                        case "y":
                            eql_2 = y
                        case "z":
                            eql_2 = z
                        case _:
                            eql = int(parsed_instruction[2])
                    match parsed_instruction[1]:
                        case "w":
                            eql_1 = w
                            if int(eql_1) == int(eql_2):
                                w = 1
                            else:
                                w = 0
                        case "x":
                            eql_1 = x
                            if eql_1 == eql_2:
                                x = 1
                            else:
                                x = 0
                        case "y":
                            eql_1 = y
                            if eql_1 == eql_2:
                                y = 1
                            else:
                                y = 0
                        case "z":
                            eql_1 = z
                            if eql_1 == eql_2:
                                z = 1
                            else:
                                z = 0
        print(f"{w=}, {x=}, {y=}, {z=}")
        if z == 0:
            break
        test_number -= test_number
        test_number_as_list = [int(x) for x in str(test_number)]
        inp_counter = 0
        if 0 in test_number_as_list:
            test_number -= test_number
            test_number_as_list = [int(x) for x in str(test_number)]
    print(f"The model number is {test_number}")


# answer is not 99999999999999 so need to check algorithm
