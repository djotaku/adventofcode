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
    if x_velocity < 0:
        x_velocity = 0
    y_velocity = current_velocity[1] - 1
    return x_pos, y_pos, x_velocity, y_velocity


if __name__ == "__main__":
    # target_parameters = input_only_one_line("../input.txt")
    target_parameters = input_only_one_line("../test_input.txt")
    regex = re.compile(r'target area: x=(\d+)..(\d+), y=(-\d+)..(-\d+)')
    target_area = re.findall(regex, target_parameters)
    x_min = int(target_area[0][0])
    x_max = int(target_area[0][1])
    y_min = int(target_area[0][3])
    y_max = int(target_area[0][2])
    velocities_that_complete = []
    current_x_pos = 0
    current_y_pos = 0
    for x in range(x_max):
        for y in range(10):
            run_sim = True
            current_x_velocity = x
            current_y_velocity = y
            print(f"testing velocities: ({current_x_velocity}, {current_y_velocity}")
            while run_sim:
                current_x_pos, current_y_pos, current_x_velocity, current_y_velocity = probe_step((current_x_pos, current_y_pos), (current_x_velocity, current_y_velocity))
                if x_min <= current_x_pos <= x_max and y_min <= current_y_pos <= y_max:
                    velocities_that_complete.append((x, y))
                    run_sim = False
                if current_x_velocity == 0 and current_x_pos < x_min:
                    run_sim = False
                if current_x_pos > x_max:
                    run_sim = False
                if current_y_pos < y_min:
                    run_sim = False
                print(current_x_pos, current_y_pos)
    print(velocities_that_complete)
