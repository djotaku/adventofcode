def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def is_this_a_triangle(side_one: int, side_two: int, side_three: int) -> int:
    """Take in triples and return 1 if a triangle."""
    if side_one + side_two > side_three and side_one + side_three > side_two and side_two + side_three > side_one:
        return 1
    else:
        return 0


if __name__ == "__main__":
    list_of_triples = input_per_line("../input.txt")
    count = 0
    for triple in list_of_triples:
        numeric_triples = [int(number) for number in triple.split()]
        count += is_this_a_triangle(numeric_triples[0], numeric_triples[1], numeric_triples[2])
    print(f"There are {count} triangles in the list when viewed as rows.")

