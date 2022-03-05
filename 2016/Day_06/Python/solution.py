"""Solution for 2016 Day 5 -- Signals and Noise."""

from collections import Counter


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_most_common_letters(word_list: list, word_length: int) -> list:
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
    return [counter_list[number].most_common(1)[0][0] for number in range(len(counter_list))]


if __name__ == '__main__':
    scrambled_signal = input_per_line("../input.txt")
    scrambled_word_length = len(scrambled_signal[0])
    most_common = find_most_common_letters(scrambled_signal, scrambled_word_length)
    print(f"The message is {''.join(most_common)}")
