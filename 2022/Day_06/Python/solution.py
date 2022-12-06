"""Solution to AoC 2022 Day 06 - Tuning Trouble."""

from collections import deque


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


if __name__ == "__main__":
    datastream = input_only_one_line("../input.txt")
    marker_check = deque(maxlen=4)
    for index, character in enumerate(datastream):
        marker_check.append(character)
        if index >= 3:
            check_set = set(marker_check)
            if len(check_set) == 4:
                print(f"We need to process {index + 1} characters to find the start-of-packet")
                break
    packet_check = deque(maxlen=14)
    for index, character in enumerate(datastream):
        packet_check.append(character)
        if index >= 13:
            check_set = set(packet_check)
            if len(check_set) == 14:
                print(f"We need to process {index + 1} characters to find the start-of-message")
                break
