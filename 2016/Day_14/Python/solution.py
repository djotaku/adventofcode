"""Solution for Advent of Code 2016: One-Time Pad."""

import hashlib
import re


def calculate_hash(text_to_hash: str) -> str:
    return hashlib.md5(text_to_hash.encode('utf-8')).hexdigest()


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
    regular_expression = re.compile(r'(%s)\1\1\1\1' % char_to_match)
    match = re.search(regular_expression, md5_hash)
    if match:
        print(match[0])
        return True
    else:
        return False


def find_one_time_pad_keys(salt: str, key_to_stop: int) -> int:
    index = 0
    key = 0
    hash_list = []
    # create first 1000 keys
    for hash_number in range(0, 1000):
        hash_list.append(calculate_hash(salt+str(hash_number)))

    while key != key_to_stop:
        triple_answer, triple_character = is_there_a_triple(hash_list[index])
        print(f"{triple_character=}")
        if triple_answer:
            for quint_index in range(index+1, len(hash_list)):
                if is_there_a_quintuple(str(triple_character), hash_list[quint_index]):
                    key += 1
                    break
        index += 1
        hash_list.append(calculate_hash(salt+str(index+999)))
    return index - 1


if __name__ == "__main__":
    pass
