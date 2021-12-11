"""Solution for Advent of Code Day 11: Dumbo Octopus"""
import logging
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


class DumboOctopus:
    """Class to hold octopus energy level and whether it has already flashed"""
    def __init__(self, initial_energy_level: int):
        self.energy_level: int = initial_energy_level
        self.flashed: bool = False


def create_octopus_grid(octopus_input: list) -> dict:
    """Take in a list of initial octopus arrangements and energy and turn into a dictionary of DumboOctopus."""
    octo_dict = {}
    for y, octopus_line in enumerate(octopus_input):
        for x, octopus in enumerate(octopus_line):
            octo_dict[(x, y)] = DumboOctopus(int(octopus))
    return octo_dict


def flash_octopuses(octopus_dictionary: dict) -> dict:
    """Flash the octopuses (recursively if necessary) and return the final octopus dictionary."""
    go_again = False
    for location, octopus in octopus_dictionary.items():
        if octopus.energy_level > 9 and octopus.flashed is False:
            logger.debug(f"I'm at {location=} and my flash status is {octopus.flashed}")
            octopus.flashed = True
            location_x = location[0]
            location_y = location[1]
            top_left = (location_x - 1, location_y - 1)
            top = (location_x, location_y - 1)
            top_right = (location_x + 1, location_y - 1)
            right = (location_x + 1, location_y)
            bottom_right = (location_x + 1, location_y + 1)
            bottom = (location_x, location_y + 1)
            bottom_left = (location_x - 1, location_y + 1)
            left = (location_x - 1, location_y)
            logger.debug(f"My neighbors are: {top_left}, {top}, {top_right}, {right}, {bottom_right}, {bottom},"
                         f" {bottom_left}, {left}")
            for neighbor in [top_left, top, top_right, right, bottom_right, bottom, bottom_left, left]:

                if neighbor in octopus_dictionary:
                    octopus_dictionary[neighbor].energy_level += 1
                    if octopus_dictionary[neighbor].flashed is False:
                        go_again = True
    if go_again:
        logger.debug("-----------------")
        logger.debug("About to do another loop")
        logger.debug("-----------------")
        return flash_octopuses(octopus_dictionary)
    return octopus_dictionary


def octopus_step(octopus_dictionary: dict) -> (dict, int):
    """Take in a dictionary of DumboOctopus and then run through a step.

    Step includes:
    - First, the energy level of each octopus increases by 1.
    - Then, any octopus with an energy level greater than 9 flashes.
    This increases the energy level of all adjacent octopuses by 1,
    including octopuses that are diagonally adjacent. If this causes an octopus
    to have an energy level greater than 9, it also flashes. This process continues as
    long as new octopuses keep having their energy level increased beyond 9.
    (An octopus can only flash at most once per step.)
    - Finally, any octopus that flashed during this step has its energy level set to 0,
    as it used all of its energy to flash.

    Return new status and number of flashes.
    """
    logger.debug("--------------------------------")
    logger.debug("Step 1: Raise Octopus energy levels")
    flash_count = 0
    # Step 1: Raise all octopus energy levels
    for octopus in octopus_dictionary.values():
        octopus.energy_level += 1
    logger.debug(f"{octopus_dictionary[(0, 0)].energy_level=}")
    logger.debug(f"{octopus_dictionary[(1, 0)].energy_level=}")
    logger.debug(f"{octopus_dictionary[(2, 0)].energy_level=}")
    # Step 2
    logger.debug("--------------------------------")
    logger.debug("Step 2: Flash the Octopuses")
    octopus_dictionary = flash_octopuses(octopus_dictionary)
    logger.debug(f"{octopus_dictionary[(0, 0)].energy_level=}")
    logger.debug(f"{octopus_dictionary[(1, 0)].energy_level=}")
    logger.debug(f"{octopus_dictionary[(2, 0)].energy_level=}")
    # Step 3
    logger.debug("--------------------------------")
    logger.debug("Step 3: Reset Flashed Octopus Energy levels to 0")
    for octopus in octopus_dictionary.values():
        if octopus.energy_level > 9:
            octopus.energy_level = 0
        if octopus.flashed:
            flash_count += 1
            octopus.flashed = False
    return octopus_dictionary, flash_count


if __name__ == "__main__":
    initial_octopus_energy = input_per_line("../input.txt")
    octopus_grid = create_octopus_grid(initial_octopus_energy)
    part_one_flashes = 0
    everyone_flash_step = 0
    for number in range(1000):
        octopus_grid, this_time_flashes = octopus_step(octopus_grid)
        if number < 100:
            part_one_flashes += this_time_flashes
        if this_time_flashes == 100:
            everyone_flash_step = number + 1
            break
    print(f"After 100 steps there have been {part_one_flashes} 🐙 flashes")
    print(f"The first time all the dumbo 🐙 (🐘🐙?) flash at once is {everyone_flash_step}")


# 23 is not the right answer
# 504 is too low