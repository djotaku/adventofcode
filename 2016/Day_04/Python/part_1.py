from collections import Counter
import re


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def create_checksum_check(the_counter):
    """Takes in a counter and sorts by amount and then alphabetical in case of a tie."""
    sorted_counter = sorted(the_counter.most_common(), key=lambda x: (-x[1], x[0]))
    # print(f"{sorted_counter=}")
    return [letter_pair[0] for letter_pair in sorted_counter]


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
    encrypted_letters_in_order = create_checksum_check(encryption_counter)
    # print(f"{encrypted_letters_in_order=}")
    # print(f"{checksum=}")
    # time to check if the checksum is right
    is_it_valid = [
        checksum[index] == encrypted_letters_in_order[index]
        for index in range(5)
    ]

    # print(f"{is_it_valid=}")
    if all(is_it_valid):
        # print(f"{sector_and_checksum_results[0][0]=}")
        return int(sector_and_checksum_results[0][0])
    else:
        return 0


if __name__ == "__main__":
    sector_id_sum = 0
    rooms_to_check = input_per_line("../input.txt")
    for room in rooms_to_check:
        # print(f"{room=}")
        sector_id_sum += is_real_room(room)
    print(f"The sum of sector ids for real rooms is {sector_id_sum}")

# 512266 is too high
