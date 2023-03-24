"""Advent of Code 2017 Day 01 - Chronal Calibration."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [eval(line.rstrip()) for line in input_file.readlines()]


def find_repeating_frequency(numbers: list[int]) -> int:
    """Go through the list over and over, summing one by one and looking for the first repeated sum.
    Then return that number.
    """
    seen_frequencies = set()
    current_frequency = 0
    searching_for_frequencies_repeated = True
    while searching_for_frequencies_repeated:
        for number in numbers:
            current_frequency += number
            if current_frequency in seen_frequencies:
                return current_frequency
            seen_frequencies.add(current_frequency)


if __name__ == "__main__":
    frequencies = input_per_line("../input.txt")
    part_one_sum = sum(frequencies)
    print(f"The resulting frequency is {part_one_sum}")
    part_two = find_repeating_frequency(frequencies)
    print(f"The first frequency reached twice is {part_two}")
