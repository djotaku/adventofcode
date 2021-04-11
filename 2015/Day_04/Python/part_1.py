import hashlib


def calculate_hash(text_to_hash):
    return hashlib.md5(text_to_hash.encode('utf-8')).hexdigest()


def does_it_lead_with_five_zeroes(hash_string):
    zero_count = 0
    for character in hash_string:
        if character == "0":
            zero_count += 1
        if character != "0":
            break
    return zero_count >= 5


def find_special_number(puzzle_text):
    decimal_number = 1
    found_it = False
    while not found_it:
        decimal_number += 1
        calculated_hash = calculate_hash(puzzle_text + str(decimal_number))
        found_it = does_it_lead_with_five_zeroes(calculated_hash)
    return decimal_number


if __name__ == "__main__":
    puzzle_input = "iwrupvqb"
    answer = find_special_number(puzzle_input)
    print(f"The number to add is {answer}")
# 346387 is too high