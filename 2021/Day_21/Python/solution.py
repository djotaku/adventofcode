"""Solution for Advent of Code 2021 Day 21: Dirac Dice """


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


class Player:
    def __init__(self, name, initial_location):
        self.player_name = name
        self.player_score = 0
        self.location = initial_location

    def move_player(self, die_roll: int):
        """Move the player from their current location to the new location."""
        location = self.location + die_roll
        # now take into account that the board is circular
        location = location % 10
        self.location = location

    def update_score(self):
        self.player_score += self.location

    def complete_move(self, die_roll: int):
        """Move player and update score"""
        self.move_player(die_roll)
        self.update_score()


class Die:
    def __init__(self):
        self.number_rolled = 0
        self.times_rolled = 0

    def next_roll(self, practice_mode=True):
        """Calculate the next roll of the die. In practice mode it's just a one-up"""
        if practice_mode:
            self.number_rolled += 1
            self.times_rolled += 1


if __name__ == "__main__":
    player_starting_positions = input_per_line("../input.txt")
    # create the players
    max_player_score = 0
    # while loop that ends when max_player_score > 999
    # roll die 3 times
    # player one
    # roll die 3 times
    # player 2
    # max_player_score = max(player_one.player_score, player_two.player_score)
    # do the calculation for the puzzle submition