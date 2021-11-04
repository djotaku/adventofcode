import string
from collections import Counter
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def create_checksum_check(the_counter):
    """Takes in a counter and sorts by amount and then alphabetical in case of a tie."""
    sorted_counter = sorted(the_counter.most_common(), key=lambda x: (-x[1], x[0]))
    return [letter_pair[0] for letter_pair in sorted_counter]


def decipher_and_discover(encrypted_room: list, sector_id: str) -> bool:
    """Return true if this is the room we want."""
    shift = int(sector_id) % 26
    alphabet = string.ascii_lowercase
    decrypted_room = ""
    for character_string in encrypted_room:
        for character in character_string:
            # where are we in the alphabet?
            character_index = alphabet.index(character)
            new_character = character_index + shift
            if new_character > 25:
                new_character = new_character - 26
            decrypted_room += alphabet[new_character]
        decrypted_room += " "
    return decrypted_room.__contains__("object")


def is_real_room(room_data: str) -> tuple[int, int]:
    """Determine if a room is real and return sector ID. Else return 0."""
    encryption_counter = Counter()
    sector_and_checksum = re.compile(r'(\d+)\[(\w+)]')
    sector_and_checksum_results = re.findall(sector_and_checksum, room_data)
    encrypted = re.compile(r'(\w+)-')
    encrypted_results = re.findall(encrypted, room_data)
    # fill out counter to figure out if the checksum is right
    for encrypted_result in encrypted_results:
        for letter in encrypted_result:
            encryption_counter[letter] += 1
    # create checksum list
    checksum = [letter for letter in sector_and_checksum_results[0][1]]
    encrypted_letters_in_order = create_checksum_check(encryption_counter)
    # time to check if the checksum is right
    is_it_valid = [
        checksum[index] == encrypted_letters_in_order[index]
        for index in range(5)
    ]
    if all(is_it_valid):
        if decipher_and_discover(encrypted_results, sector_and_checksum_results[0][0]):
            return int(sector_and_checksum_results[0][0]), int(sector_and_checksum_results[0][0])
        else:
            return int(sector_and_checksum_results[0][0]), 0
    else:
        return 0, 0


if __name__ == "__main__":
    part_1sector_ids = []
    part_two_sector_id = []
    rooms_to_check = input_per_line("../input.txt")
    for room in rooms_to_check:
        part_1, part_2 = is_real_room(room)
        part_1sector_ids.append(part_1)
        part_two_sector_id.append(part_2)
    sector_id_sum = sum(part_1sector_ids)
    part_two_answer = sum(part_two_sector_id)
    print(f"The sum of sector ids for real rooms is {sector_id_sum}")
    print(f"The sector ID of the decrypted room is {part_two_answer}")

# 512266 is too high
