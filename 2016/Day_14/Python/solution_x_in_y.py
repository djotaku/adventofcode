"""Solution for Advent of Code 2016: One-Time Pad testing optimizations."""

import hashlib
import re


def calculate_hash(text_to_hash: str) -> str:
    return hashlib.md5(text_to_hash.encode('utf-8')).hexdigest()


def part_two_hash(text_to_hash: str) -> str:
    for hashes in range(0, 2017):
        text_to_hash = calculate_hash(text_to_hash)
    return text_to_hash


def is_there_a_triple(md5_hash: str) -> (bool, str):
    """Check an MD5 Hash to see if there's a triple in it. Return the character that's in the triple."""
    regular_expression = re.compile(r'(\S)\1\1')
    match = re.search(regular_expression, md5_hash)
    if match:
        return True, match[0][0]
    else:
        return False, ""


def is_there_a_quintuple(char_to_match: str, md5_hash: str) -> bool:
    """Check to see if there is a quintuple featuring the char_to_match"""
    quintuple = char_to_match * 5
    if quintuple in md5_hash:
        return True
    else:
        return False


def find_one_time_pad_keys(salt: str, key_to_stop: int, part_two: bool = False) -> int:
    index = 0
    key = 0
    hash_list = []
    # create first 1000 keys
    for hash_number in range(0, 1000):
        if part_two:
            hash_list.append(part_two_hash(salt + str(hash_number)))
        else:
            hash_list.append(calculate_hash(salt + str(hash_number)))

    while key != key_to_stop:
        triple_answer, triple_character = is_there_a_triple(hash_list[index])
        if triple_answer:
            for quint_index in range(index + 1, len(hash_list)):
                if is_there_a_quintuple(str(triple_character), hash_list[quint_index]):
                    key += 1
                    break
        index += 1
        if part_two:
            hash_list.append(part_two_hash(salt + str(index + 999)))
        else:
            hash_list.append(calculate_hash(salt + str(index + 999)))
    return index - 1


if __name__ == "__main__":
    our_salt = "ihaygndm"
    sixty_fourth_index = find_one_time_pad_keys(our_salt, 64)
    print(f"With our salt, the 64th key for the one-time pad is {sixty_fourth_index}")
    part_two_answer = find_one_time_pad_keys(our_salt, 64, part_two=True)
    print(f"With our salt, the 64th stretched key for the one-time pad is {part_two_answer}")
