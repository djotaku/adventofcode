"""Solution to AoC 2022 Day 02 - Rock Paper Scissors."""


def process_strategy_guide(input_file: str) -> list:
    """Read in strategy guide input and output a list where the
    player's choices are split into sub-lists"""
    with open(input_file) as file:
        return [this_round.split() for this_round in file]


def calculate_win(turn: list) -> bool:
    """Return true if the player wins."""
    pass


def calculate_turn_points(turn: list) -> int:
    """Calculate the points for the chosen strategy plus whether the player won."""
    pass


if __name__ == "__main__":
    # read input
    # cycle through the parsed input with calculate_turn_points
    # either append into a list and sum or keep a sum going the whole time
    pass
