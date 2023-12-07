"""Solution for AoC 2023 # Day 6: Wait For It."""
import re
from functools import reduce
import operator

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_button_presses(race_time: int, record_distance: int) -> int:
    """Figure out how many different button press lengths can beat the record distance."""
    # this is a naive version that may fail on the full input.
    # if the naive version doesn't work, cut out (return) once you start falling below the
    # record distance again.
    successful_button_presses = 0
    for button_press_time in range(race_time):
        race_time_left = race_time - button_press_time
        distance = race_time_left * button_press_time
        if distance > record_distance:
            successful_button_presses += 1
    return successful_button_presses


if __name__ == '__main__':
    race_records = input_per_line("../sample_input.txt")
    regex = re.compile(r'\d+')
    times = re.findall(regex, race_records[0])
    distances = re.findall(regex, race_records[1])
    button_press_amounts = []
    for number in range(len(times)):
        button_press_amounts.append(find_button_presses(int(times[number]), int(distances[number])))
    product = reduce(operator.mul, button_press_amounts, 1)
    print(f"If you multiply winning button presses together you get {product}")
