"""Solution for 2016 Day 5 -- Signals and Noise."""

from collections import Counter


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def decrypt_message(word_list: list, word_length: int) -> tuple:
    """Take in a list of words, count the number of times each letter appears per position.

    :param word_list: the words to search.
    :param word_length: how long each of the words are
    :return: list of characters that appear most often in each position
    """
    counter_list = [Counter() for number in range(word_length)]
    for word in word_list:
        characters = [character for character in word]
        for position, character in enumerate(characters):
            counter_list[position][character] += 1
    most_common_letters = [counter_list[number].most_common(1)[0][0] for number in range(len(counter_list))]
    least_common_letters = [list(reversed(counter_list[number].most_common()))[0][0] for number in range(len(counter_list))]
    return most_common_letters, least_common_letters


if __name__ == '__main__':
    scrambled_signal = input_per_line("../input.txt")
    scrambled_word_length = len(scrambled_signal[0])
    most_common, least_common = decrypt_message(scrambled_signal, scrambled_word_length)
    print(f"The first message is {''.join(most_common)}")
    print(f"The second message is {''.join(least_common)}")
