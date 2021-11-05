"""AoC 2016 Day 05 Python Solution."""
import hashlib


def calculate_hash(text_to_hash):
    return hashlib.md5(text_to_hash.encode('utf-8')).hexdigest()


def does_it_lead_with_five_zeroes(hash_string):
    """Figure out if you have a hash that starts with 5 zeroes."""
    zero_count = 0
    for character in hash_string:
        if character == "0":
            zero_count += 1
        if character != "0":
            break
    return zero_count >= 5


def door_password(puzzle_text):
    decimal_number = 0
    password = ""
    while len(password) < 8:
        decimal_number += 1
        calculated_hash = calculate_hash(puzzle_text + str(decimal_number))
        if does_it_lead_with_five_zeroes(calculated_hash):
            password += calculated_hash[5]
    return password


if __name__ == "__main__":
    puzzle_input = "ugkcyxxp"
    answer = door_password(puzzle_input)
    print(f"The number to add is {answer}")

# Part 1: 836bc9123 is not right nor is 836bc912