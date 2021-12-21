"""Solution for Advent of Code 2021 Day 21: Dirac Dice """


class Player:
    def __init__(self, name):
        self.player_name = name
        self.player_score = 0


class Die:
    def __init__(self):
        self.number_rolled = 1

    def next_roll(self, practice_mode=True):
        """Calculate the next roll of the die. In practice mode it's just a one-up"""
        if practice_mode:
            self.number_rolled += 1


class GameBoard:
    def __init__(self, player_one: Player, player_one_location: int,
                 player_two: Player, player_two_location: int):
        self.player_one = player_one
        self.player_two = player_two
