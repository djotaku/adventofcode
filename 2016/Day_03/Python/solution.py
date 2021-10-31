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
    part_two_count = 0
    column_one = []
    column_two = []
    column_three = []
    for triple in list_of_triples:
        numeric_triples = [int(number) for number in triple.split()]
        column_one.append(numeric_triples[0])
        column_two.append(numeric_triples[1])
        column_three.append(numeric_triples[2])
    for index in range(0, len(column_one), 3):
        part_two_count += is_this_a_triangle(column_one[index], column_one[index+1], column_one[index+2])
        part_two_count += is_this_a_triangle(column_two[index], column_two[index+1], column_two[index+2])
        part_two_count += is_this_a_triangle(column_three[index], column_three[index+1], column_three[index+2])
    print(f"There are {part_two_count} triangles in the list when viewed as columns.")

# 4174 is too high
# 0 is not answer
# 1918 is too low
