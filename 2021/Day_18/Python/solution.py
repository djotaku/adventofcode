"""Solution for Advent of Code Day 18: Snailfish."""


def snailfish_addition(number_one: str, number_two: str) -> str:
    """Take in 2 snailfish numbers and add them together. Do not worry about reduction. That will be a later step."""
    return f"[{number_one},{number_two}]"


def snailfish_reduction(snailfish_number: str) -> str:
    """Take in a snailfish number and keep reducing until no more reductions are necessary."""
    number_as_list = [character for character in snailfish_number]
    # Test for need for explosion
    left_bracket_count = 0
    current_left_number = None
    for index, character in enumerate(number_as_list):
        if character == "[":
            left_bracket_count += 1
        if character == "]":
            left_bracket_count == 0
        if character.isdigit():
            current_left_number = character
        if left_bracket_count == 5:
            # explode and recurse
            # first deal with left number
            resultant_left_number = 0
            if current_left_number == None:
                resultant_left_number = 0
            else:
                resultant_left_number = current_left_number + number_as_list[index + 1]

            pass

    # Test for Split
    # Return answer


