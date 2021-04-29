"""Find length of the a number after a look-and-say game."""
import re


def create_number_lists(game_input):
    combined_list = []
    for number in game_input:
        if len(game_input) == 1:
            return [number]

