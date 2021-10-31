from collections import Counter
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def is_real_room(room_data: str) -> int:
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
    encrypted_letters_in_order = [letter_pair[0] for letter_pair in encryption_counter.most_common()]
    # time to check if the checksum is right
    is_it_valid = [True for index in range(5) if checksum[index] == encrypted_letters_in_order[index]]
    if all(is_it_valid):
        return sector_and_checksum_results[0][0]
    else:
        return 0
    #print(f"{sector_and_checksum_results=} and {encrypted_results=}")
    #print(encrypted_letters_in_order)


if __name__ == "__main__":
    print(is_real_room("aaaaa-bbb-z-y-x-123[abxyz]"))
