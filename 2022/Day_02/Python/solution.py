"""Solution to AoC 2022 Day 02 - Rock Paper Scissors."""


def process_strategy_guide(input_file: str) -> list:
    """Read in strategy guide input and output a list where the
    player's choices are split into sub-lists"""
    with open(input_file) as file:
        return [this_round.split() for this_round in file]


def calculate_win(turn_for_eval: list) -> int:
    """Return points if the player wins or draws."""
    if turn_for_eval[0] == "A":
        if turn_for_eval[1] == "X":  # Rock/Rock - tie
            return 3
        elif turn_for_eval[1] == "Y":  # Rock/Paper - win
            return 6
        else:  # Rock/scissors - lose
            return 0
    elif turn_for_eval[0] == "B":  # Paper
        if turn_for_eval[1] == "X":  # Paper/Rock - lose
            return 0
        elif turn_for_eval[1] == "Y":  # Paper/Paper - tie
            return 3
        else:  # Paper/Scissors - win
            return 6
    else:  # Scissors
        if turn_for_eval[1] == "X":  # Scissors/Rock - win
            return 6
        elif turn_for_eval[1] == "Y":  # Scissors/Paper - lose
            return 0
        else:  # Scissors/Scissors - tie
            return 3


def calculate_turn_points(turn: list) -> int:
    """Calculate the points for the chosen strategy plus whether the player won."""
    shape_points = {"X": 1, "Y": 2, "Z": 3}
    return shape_points[turn[1]] + calculate_win(turn)


if __name__ == "__main__":
    # read input
    # cycle through the parsed input with calculate_turn_points
    # either append into a list and sum or keep a sum going the whole time
    strategy_guide = process_strategy_guide("../input.txt")
    turn_totals = [calculate_turn_points(turn) for turn in strategy_guide]
    total_score = sum(turn_totals)
    print(f"Following the strategy guide will yield a total score of {total_score}.")
