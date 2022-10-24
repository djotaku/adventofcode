"""Solution for AoC 2016 Day 15: Timing is Everything"""
import re


def find_capsule_time(discs: list) -> int:
    """Figure out what time to start the machine.

    discs list should contain tuples: (positions, starting position)

    Order matters, it should be the order of discs in the machine.
    """
    # reaches the first disc at t=1.
    time = 0
    loop = True
    drop_check = []
    while loop:
        time += 1
        for time_delta, disc in enumerate(discs, start=1):
            if (disc[1] + time + time_delta) % disc[0] == 0:
                drop_check.append(True)
            else:
                drop_check.append(False)
        if all(drop_check):
            loop = False
        drop_check.clear()
    return time


def extract_data(puzzle_input: list) -> list:
    """Take in a list where each item looks like:

    Disc #1 has 5 positions: at time=0, it is at position 4.

    and returns a list with items like (based on above):

    (5, 4)
    """
    regex = re.compile(r'(\d+) positions; at time=0, it is at position (\d+)')
    output_list = []
    for sentence in puzzle_input:
        numbers = re.findall(regex, sentence)
        # print(f"{numbers=}")
        output_list.append((int(numbers[0][0]), int(numbers[0][1])))
    return output_list


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


if __name__ == "__main__":
    our_input = input_per_line('../input.txt')
    # print(f"{our_input=}")
    our_extracted_data = extract_data(our_input)
    # print(f"{our_extracted_data=}")
    start_time = find_capsule_time(our_extracted_data)
    print(f"To get the capsule to the bottom, we should push start at {start_time}")
