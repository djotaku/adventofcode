"""Solution to AoC 2022 Day 15 - Beacon Exclusion Zone."""
import re
from collections import namedtuple


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


Coordinate = namedtuple('Point', ['x', 'y'])


def extract_coordinates(location: str) -> Coordinate:
    """Take in a sentence like:

    Sensor at x=2, y=18: closest beacon is at x=-2, y=15

    and returns 2 named tuples of type Coordinate.
    """
    regex = re.compile(r'(-*\d+)')
    coordinates = re.findall(regex, location)
    # print(coordinates)
    return Coordinate(int(coordinates[0]), int(coordinates[1])), Coordinate(int(coordinates[2]), int(coordinates[3]))


def calculate_taxi_distance(sensor_coord: Coordinate, beacon_coord: Coordinate) -> int:
    """Take in 2 coordinates and calculate the taxi (or Manhattan) distance"""
    return abs(sensor_coord.x - beacon_coord.x) + abs(sensor_coord.y - beacon_coord.y)


def find_beacon_exclusion_zone(sensor_coord: Coordinate, taxi_distance: int, beacon_coord: Coordinate, y: int) -> set:
    """Find all the areas there can't be a beacon.

    Based on understanding of the problem prompt, remove the beacon that we know about.
    """
    non_beacon_coordinates = set()
    top_coordinate = Coordinate(sensor_coord.x, (sensor_coord.y - taxi_distance))
    # print(f"{top_coordinate=}")
    non_beacon_coordinates.add(top_coordinate)
    # top half
    for delta_y in range(1, taxi_distance + 1):
        new_y = top_coordinate.y + delta_y
        # print(f"{new_y=}")
        for delta_x in range(-(delta_y), taxi_distance + (new_y - sensor_coord.y) + 1):
            new_x = top_coordinate.x + delta_x
            # print(f"({new_x}, {new_y})")
            if new_y == y:
                non_beacon_coordinates.add(Coordinate(new_x, new_y))
    # bottom half
    for delta_y in range(taxi_distance+1, (taxi_distance*2) + 1):
        new_y = top_coordinate.y + delta_y
        # print(f"{delta_y=}")
        # print(f"{new_y=}")
        # print(-(taxi_distance - (new_y - sensor_coord.y)))
        for delta_x in range(-(taxi_distance - (new_y - sensor_coord.y)), taxi_distance - (new_y - sensor_coord.y)+1):
            new_x = top_coordinate.x + delta_x
            # print(f"{new_x=}, {new_y=}")
            if new_y == y:
                non_beacon_coordinates.add(Coordinate(new_x, new_y))
    if beacon_coord in non_beacon_coordinates:
        non_beacon_coordinates.remove(beacon_coord)
    return non_beacon_coordinates

def simplified_part_1(taxi_distance: int, y_value: int, sensor_coord: Coordinate, beacon_coord: Coordinate) -> int:
    """Take in taxi distance, sensor, beacon, and a y value and calcluate all the non-beacon spots."""
    # does this sensor have an exclusion zone in the y-space we care about?
    number_of_x = 0
    if (sensor_coord.y - taxi_distance) <= y_value <= (sensor_coord.y + taxi_distance):
        x_value = abs(y_value) - taxi_distance
        number_of_x = x_value * 2
    if beacon_coord.y == y_value:
        number_of_x -= 1
    return number_of_x

if __name__ == "__main__":
    debug = False
    if debug:
        file = "../sample_input.txt"
        y_we_care_about = 10
    else:
        file = "../input.txt"
        y_we_care_about = 2000000
    all_the_coordinates = input_per_line(file)
    empty_area_tally = 0
    total_empty_area = set()
    # all_the_coordinates = ["Sensor at x=8, y=7: closest beacon is at x=2, y=10"]
    # old way
    #for coordinate_pair in all_the_coordinates:
    #    sensor, beacon = extract_coordinates(coordinate_pair)
    #    # print(f"{sensor=}")
    #    manhattan_distance = calculate_taxi_distance(sensor, beacon)
    #    no_beacons = find_beacon_exclusion_zone(sensor, manhattan_distance, beacon, y_we_care_about)
    #    # print(f"size of no_beacons: {len(no_beacons)}")
    #    for coordinate in no_beacons:
    #        if coordinate.y == y_we_care_about:
    #            total_empty_area.add(coordinate)
    # new way
    for coordinate_pair in all_the_coordinates:
        sensor, beacon = extract_coordinates(coordinate_pair)
    #    # print(f"{sensor=}")
        manhattan_distance = calculate_taxi_distance(sensor, beacon)
        empty_area_tally += simplified_part_1(manhattan_distance, y_we_care_about, sensor, beacon)
    print(f"There are {empty_area_tally} positions that cannot have a beacon present.")
