"""Solution for Advent of Code Day 17: Trick Shot."""
import re
import logging
logger_17 = logging.getLogger("Day_17")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()
