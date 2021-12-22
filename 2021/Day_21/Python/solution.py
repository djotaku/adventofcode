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
        # now take into account that the board is circular
        location = self.location + die_roll
        while location > 10:
            location = location - 10
        self.location = location

    def update_score(self):
        self.player_score += self.location

    def complete_move(self, die_roll: int):
        """Move player and update score"""
        self.move_player(die_roll)
        self.update_score()

    def __repr__(self):
        return f"{self.player_name} at {self.location} with score: {self.player_score}"


class Die:
    def __init__(self):
        self.number_rolled = 0
        self.times_rolled = 0

    def next_roll(self, practice_mode=True):
        """Calculate the next roll of the die. In practice mode it's just a one-up"""
        if practice_mode:
            self.number_rolled += 1
            self.times_rolled += 1
        return self.number_rolled

    def __repr__(self):
        return f"Die rolled {self.times_rolled} times. Most recent number rolled {self.number_rolled}"


if __name__ == "__main__":
    player_starting_positions = input_per_line("../input.txt")
    # create the players
    _, player_one_starting_position = player_starting_positions[0].split(":")
    player_one_starting_position = int(player_one_starting_position)
    _, player_two_starting_position = player_starting_positions[1].split(":")
    player_two_starting_position = int(player_two_starting_position)
    player_one = Player("Player 1", player_one_starting_position)
    player_two = Player("Player 2", player_two_starting_position)
    max_player_score = 0
    # create die
    part_one_die = Die()
    # while loop that ends when max_player_score > 999
    print("About to start game")
    print(player_one)
    print(player_two)
    while max_player_score < 1000:
        print("-------")
        print("New Round")
        # roll die 3 times
        rolls = [part_one_die.next_roll(practice_mode=True), part_one_die.next_roll(practice_mode=True),
                 part_one_die.next_roll(practice_mode=True)]
        player_one_moves = sum(rolls)
        print(f"{player_one_moves=}")
        player_one.complete_move(player_one_moves)
        if player_one.player_score > 999:
            break
        rolls.clear()
        rolls = [part_one_die.next_roll(practice_mode=True), part_one_die.next_roll(practice_mode=True),
                 part_one_die.next_roll(practice_mode=True)]
        player_two_moves = sum(rolls)
        player_two.complete_move(player_two_moves)
        rolls.clear()
        print(player_one)
        print(player_two)
        max_player_score = max(player_one.player_score, player_two.player_score)
    # someone has scored 1000
    print("Game Over.")
    print(player_one)
    print(player_two)
    print(part_one_die)
    loser_score = min(player_one.player_score, player_two.player_score)
    die_rolls = part_one_die.times_rolled
    print(f"Loser score times number of die rolls is {loser_score * die_rolls}")


# 1080000 is too high