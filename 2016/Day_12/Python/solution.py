"""Solution to Advent of Code 2016 Day 12: Leonardo's Monorail."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


if __name__ == "__main__":
    our_input = input_per_line('../input.txt')
    a, b, c, d, = (0, 0, 0, 0)
    counter = 0
    while counter < len(our_input):
        # print(f"{counter=}")
        # print(f"{a=}, {b=}, {c=}, {d=}, ")
        components = our_input[counter].split()
        # print(components)
        instruction = components[0]
        x = components[1]
        y = 0
        if len(components) == 3:
            y = components[2]
        match instruction:
            case "cpy":
                match x:
                    case "a":
                        left_side = a
                    case "b":
                        left_side = b
                    case "c":
                        left_side = c
                    case "d":
                        left_side = d
                    case _:
                        left_side = int(x)
                match y:
                    case "a":
                        a = left_side
                    case "b":
                        b = left_side
                    case "c":
                        c = left_side
                    case "d":
                        d = left_side
                counter += 1
            case "inc":
                match x:
                    case "a":
                        a += 1
                    case "b":
                        b += 1
                    case "c":
                        c += 1
                    case "d":
                        d += 1
                counter += 1
            case "dec":
                match x:
                    case "a":
                        a -= 1
                    case "b":
                        b -= 1
                    case "c":
                        c -= 1
                    case "d":
                        d -= 1
                counter += 1
            case "jnz":
                match x:
                    case "a":
                        number = a
                    case "b":
                        number = b
                    case "c":
                        number = c
                    case "d":
                        number = d
                    case _:
                        number = int(x)
                if number != 0:
                    counter += int(y)
                else:
                    counter += 1
    print("Part 1:")
    print(f"{a=}, {b=}, {c=}, {d=}")
    a, b, c, d, = (0, 0, 1, 0)
    counter = 0
    while counter < len(our_input):
        # print(f"{counter=}")
        # print(f"{a=}, {b=}, {c=}, {d=}, ")
        components = our_input[counter].split()
        # print(components)
        instruction = components[0]
        x = components[1]
        y = 0
        if len(components) == 3:
            y = components[2]
        match instruction:
            case "cpy":
                match x:
                    case "a":
                        left_side = a
                    case "b":
                        left_side = b
                    case "c":
                        left_side = c
                    case "d":
                        left_side = d
                    case _:
                        left_side = int(x)
                match y:
                    case "a":
                        a = left_side
                    case "b":
                        b = left_side
                    case "c":
                        c = left_side
                    case "d":
                        d = left_side
                counter += 1
            case "inc":
                match x:
                    case "a":
                        a += 1
                    case "b":
                        b += 1
                    case "c":
                        c += 1
                    case "d":
                        d += 1
                counter += 1
            case "dec":
                match x:
                    case "a":
                        a -= 1
                    case "b":
                        b -= 1
                    case "c":
                        c -= 1
                    case "d":
                        d -= 1
                counter += 1
            case "jnz":
                match x:
                    case "a":
                        number = a
                    case "b":
                        number = b
                    case "c":
                        number = c
                    case "d":
                        number = d
                    case _:
                        number = int(x)
                if number != 0:
                    counter += int(y)
                else:
                    counter += 1
    print("Part 2:")
    print(f"{a=}, {b=}, {c=}, {d=}")
