"""Advent of Code 2021 Day 01 Solution"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def part_one_sonar(part_one_sonar_measurements):
    increase_count = 0
    previous_measurement = int(part_one_sonar_measurements[0])
    for index in range(1, len(part_one_sonar_measurements)):
        current_measurement = int(part_one_sonar_measurements[index])
        if current_measurement > previous_measurement:
            increase_count += 1
        previous_measurement = current_measurement
    return increase_count


def part_two_sonar(part_two_sonar_measurements):
    increase_count = 0
    previous_triple = int(part_two_sonar_measurements[0]) + int(part_two_sonar_measurements[1]) + \
                      int(part_two_sonar_measurements[2])
    for index in range(1, len(part_two_sonar_measurements)-2):
        current_triple = int(part_two_sonar_measurements[index]) + int(part_two_sonar_measurements[index+1]) + \
                      int(part_two_sonar_measurements[index+2])
        if current_triple > previous_triple:
            increase_count += 1
        previous_triple = current_triple
    return increase_count


if __name__ == "__main__":
    sonar_measurements = input_per_line("../input.txt")
    part_one_answer = part_one_sonar(sonar_measurements)
    part_two_answer = part_two_sonar(sonar_measurements)
    print(f"There are {part_one_answer} measurements larger than the previous one.")
    print(f"If measuring by triples, {part_two_answer} measurements are larger than the previous one.")


