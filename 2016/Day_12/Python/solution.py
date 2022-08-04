"""Solution to Advent of Code 2016 Day 12: Leonardo's Monorail."""


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


def evaluate_instruction(a: int, b: int, c: int, d: int,
                         instruction: str, x: [int | str], y: [int | str] = 0) -> (int, int, int, int):
    """Take in the current register values and instructions and output the new register values."""
    match instruction:
        case "cpy":
            pass
        case "inc":
            match x:
                case "a":
                    a = a + 1
                case "b":
                    b = b + 1
                case "c":
                    c = c + 1
                case "d":
                    d = d + 1
        case "dec":
            match x:
                case "a":
                    a = a - 1
                case "b":
                    b = b - 1
                case "c":
                    c = c - 1
                case "d":
                    d = d - 1
        case "jnz":
            pass
    return a, b, c, d


if __name__ == "__main__":
    our_input = input_only_one_line("../input.txt")
