"""Advent of Code 2021 Day 01 Solution"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


if __name__ == "__main__":
    sonar_measurements = input_per_line("../input.txt")
    increase_count = 0
    previous_measurement = int(sonar_measurements[0])
    for index in range(1, len(sonar_measurements)):
        current_measurement = int(sonar_measurements[index])
        if current_measurement > previous_measurement:
            increase_count += 1
        previous_measurement = current_measurement
    print(f"There are {increase_count} measurements larger than the previous one.")


