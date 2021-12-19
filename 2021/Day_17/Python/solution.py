"""Solution for Advent of Code Day 17: Trick Shot."""
import re
import logging
logger_17 = logging.getLogger("Day_17")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


def probe_step(current_location: tuple, current_velocity: tuple) -> (tuple, tuple):
    """Take in current location and velocity and return new location and velocity."""
    x_pos = current_location[0] + current_velocity[0]
    y_pos = current_location[1] + current_velocity[1]
    x_velocity = current_velocity[0] - 1
    x_velocity = max(x_velocity, 0)
    y_velocity = current_velocity[1] - 1
    return x_pos, y_pos, x_velocity, y_velocity


def find_highest_y(valid_velocities: list) -> int:
    """Take in a list of valid velocities and figure out the highest y reached.

    Assumption for part 1: I don't think the actual velocity matters, so just look for highest
    number.
    """
    y_values = []
    for velocity in valid_velocities:
        x_velocity = velocity[0]
        y_velocity = velocity[1]
        current_x_pos = 0
        current_y_pos = 0
        while current_y_pos > -1:
            current_x_pos, current_y_pos, x_velocity, y_velocity = probe_step(
                    (current_x_pos, current_y_pos), (x_velocity, y_velocity))
            y_values.append(current_y_pos)
    logger_17.debug(y_values)
    return max(y_values)


def run_the_sim(x_min: int, x_max: int, y_min: int, y_max) -> list:
    """Take in boundary conditions for the target area and run the sim.

    Return valid velocities in a list
    """
    velocities_that_complete = []
    for x in range(x_max):
        print(f"{x=}")
        for y in range(100):
            run_sim = True
            current_x_velocity = x
            current_y_velocity = y
            current_x_pos = 0
            current_y_pos = 0
            while run_sim:
                current_x_pos, current_y_pos, current_x_velocity, current_y_velocity = probe_step(
                    (current_x_pos, current_y_pos), (current_x_velocity, current_y_velocity))
                if (
                    x_min <= current_x_pos <= x_max
                    and y_min >= current_y_pos >= y_max
                ):
                    velocities_that_complete.append((x, y))
                    run_sim = False
                if current_x_velocity == 0 and current_x_pos < x_min:
                    run_sim = False
                if current_x_pos > x_max:
                    run_sim = False
                if current_y_pos < y_max:
                    run_sim = False
    return velocities_that_complete


if __name__ == "__main__":
    target_parameters = input_only_one_line("../input.txt")
    # target_parameters = input_only_one_line("../test_input.txt")
    regex = re.compile(r'target area: x=(\d+)..(\d+), y=(-\d+)..(-\d+)')
    target_area = re.findall(regex, target_parameters)
    extracted_x_min = int(target_area[0][0])
    extracted_x_max = int(target_area[0][1])
    extracted_y_min = int(target_area[0][3])
    extracted_y_max = int(target_area[0][2])
    the_valid_velocities = run_the_sim(extracted_x_min, extracted_x_max, extracted_y_min, extracted_y_max)
    logger_17.debug(the_valid_velocities)
    part_1_answer = find_highest_y(the_valid_velocities)
    print(f"The highest y-value is {part_1_answer}")


# not 45