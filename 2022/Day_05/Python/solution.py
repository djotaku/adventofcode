"""Solution for AoC 2022 Day 05 - Supply Stacks """
import re
from collections import deque


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


crates = {
    1: deque(["D", "T", "W", "N", "L"]),
    2: deque(["H", "P", "C"]),
    3: deque(["J", "M", "G", "D", "N", "H", "P", "W"]),
    4: deque(["L", "Q", "T", "N", "S", "W", "C"]),
    5: deque(["N", "C", "H", "P"]),
    6: deque(["B", "Q", "W", "M", "D", "N", "H", "T"]),
    7: deque(["L", "S", "G", "J", "R", "B", "M"]),
    8: deque(["T", "R", "B", "V", "G", "W", "N", "Z"]),
    9: deque(["L", "P", "N", "D", "G", "W"])
}

initial_crates_two = {
    1: deque(["D", "T", "W", "N", "L"]),
    2: deque(["H", "P", "C"]),
    3: deque(["J", "M", "G", "D", "N", "H", "P", "W"]),
    4: deque(["L", "Q", "T", "N", "S", "W", "C"]),
    5: deque(["N", "C", "H", "P"]),
    6: deque(["B", "Q", "W", "M", "D", "N", "H", "T"]),
    7: deque(["L", "S", "G", "J", "R", "B", "M"]),
    8: deque(["T", "R", "B", "V", "G", "W", "N", "Z"]),
    9: deque(["L", "P", "N", "D", "G", "W"])
}

regex = re.compile(r'move (\d+) from (\d+) to (\d+)')

if __name__ == "__main__":
    instructions = input_per_line("../moves.txt")
    for instruction in instructions:
        numbers = re.findall(regex, instruction)
        crates_to_move = int(numbers[0][0])
        origin = int(numbers[0][1])
        destination = int(numbers[0][2])
        for crate_index in range(crates_to_move):
            crate = crates[origin].popleft()
            crates[destination].appendleft(crate)
    top_crates = [crate[0] for crate in crates.values()]
    top_crates_text = "".join(top_crates)
    print(f"The top crates spell {top_crates_text}")
    for instruction in instructions:
        numbers = re.findall(regex, instruction)
        crates_to_move = int(numbers[0][0])
        origin = int(numbers[0][1])
        destination = int(numbers[0][2])
        part_two_crates = []
        for crate_index in range(crates_to_move):
            part_two_crates.append(initial_crates_two[origin].popleft())
        for crate in reversed(part_two_crates):
            initial_crates_two[destination].appendleft(crate)
    top_crates_part_two = [crate[0] for crate in initial_crates_two.values()]
    top_creates_part_two_text = "".join(top_crates_part_two)
    print(f"The top creates spell {top_creates_part_two_text}")