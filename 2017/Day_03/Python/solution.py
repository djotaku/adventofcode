"""Solution to AoC 2017 Day 03 - Spiral Memory."""
import math

if __name__ == "__main__":
    puzzle_input = 277678
    puzzle_input = 23
    puzzle_square_root = math.sqrt(puzzle_input)
    square_root_floor = math.floor(puzzle_square_root)
    distance_from_one = square_root_floor//2
    starting_coordinate = (distance_from_one, distance_from_one)
    y_diff = puzzle_input - square_root_floor**2
    puzzle_coordinate = (distance_from_one, distance_from_one+y_diff)
    distance_from_center = abs(puzzle_coordinate[0]-puzzle_coordinate[1])
    print(distance_from_center)
