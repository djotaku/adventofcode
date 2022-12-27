"""Solution to AoC 2017 Day 04 - High-Entropy Passphrases"""

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

def check_passphrase(passphrase: str) -> bool:
    """Return true if it's a valid passphrase."""
    words = passphrase.split()
    test_set = set()
    for word in words:
        test_set.add(word)
    if len(test_set) == len(words):
        return True
    else:
        return False


def check_anagrams(passphrase: str) -> bool:
    """Return True if there aren't any anagrams."""
    words = passphrase.split()
    letter_list = []
    for word in words:
        set_to_check = set()
        for letter in word:
            set_to_check.add(letter)
        letter_list.append(set_to_check)
    letter_list_len = len(letter_list)
    while letter_list_len > 0:
        comparison_set = letter_list.pop()
        popped_list_len = len(letter_list)
        for index in range(popped_list_len):
            if comparison_set == letter_list[index]:
                return False
        letter_list_len = len(letter_list)
    return True


if __name__ == "__main__":
    passphrases = input_per_line("../input.txt")
    validated_phrases = [1 for phrase in passphrases if check_passphrase(phrase)]
    print(f"There were {sum(validated_phrases)} valid phrases.")
    part_2_validated_phrases = [1 for phrase in passphrases if check_anagrams(phrase)]
    print(f"There were {sum(part_2_validated_phrases)} valid phrases.")


# 477 too high