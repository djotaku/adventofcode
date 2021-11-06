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


def door_2_password(puzzle_text):
    """Generate the password for the second door at Easter Bunny HQ."""
    door_two_password = [None, None, None, None, None, None, None, None]
    decimal_number = 0
    while None in door_two_password:
        decimal_number += 1
        calculated_hash = calculate_hash(puzzle_text + str(decimal_number))
        if does_it_lead_with_five_zeroes(calculated_hash):
            try:
                position = int(calculated_hash[5])
            except:
                # this is to catch a letter in the sixth position
                position = 9
            if position < 8 and door_two_password[position] is None:
                door_two_password[position] = calculated_hash[6]
    return ''.join(door_two_password)


if __name__ == "__main__":
    puzzle_input = "ugkcyxxp"
    answer = door_password(puzzle_input)
    second_password = door_2_password(puzzle_input)
    print(f"The password to door number one is {answer}")
    print(f"The password to door number two is {second_password}")

# Part 1: 836bc9123 is not right nor is 836bc912
# Part 2: 1cc70965 is not the right answer