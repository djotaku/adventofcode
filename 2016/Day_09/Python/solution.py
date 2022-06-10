"""Solution to Advent of Code 2016 Day 09: Explosives in Cyberspace"""


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


def decompress_string(input_string: str) -> str:
    """Take in a string and run the decompression algorithm.

    Return the decompressed string.
    """
    characters = list(input_string)
    are_we_in_data = False
    are_we_in_marker = False
    position_in_character_list = 0
    output_string = ""
    current_marker = ""
    characters_to_repeat = 0
    repetitions = 0
    repetition_string = ''
    while position_in_character_list < len(characters):
        if are_we_in_data is False and are_we_in_marker is False:
            if characters[position_in_character_list] == '(':
                are_we_in_marker = True
            else:
                output_string += characters[position_in_character_list]
            position_in_character_list += 1
        elif are_we_in_marker is True:
            if characters[position_in_character_list] != ')':
                current_marker += characters[position_in_character_list]
            else:
                are_we_in_data = True
                are_we_in_marker = False
                split_marker = current_marker.split('x')
                characters_to_repeat = int(split_marker[0])
                repetitions = int(split_marker[1])
                current_marker = ''
            position_in_character_list += 1
        elif are_we_in_data is True:
            while characters_to_repeat > 0:
                repetition_string += characters[position_in_character_list]
                position_in_character_list += 1
                characters_to_repeat -= 1
            while repetitions > 0:
                output_string += repetition_string
                repetitions -= 1
            are_we_in_data = False
            repetition_string = ""
    return output_string


def decompress_version_2(input_string: str) -> int:
    """Take in a string and output the decompressed length."""
    characters = list(input_string)
    length = 0
    are_we_in_marker = False
    position_in_character_list = 0
    current_marker = ""
    while position_in_character_list < len(characters):
        if not are_we_in_marker:
            if characters[position_in_character_list] != "(":
                length += 1
                position_in_character_list += 1
            else:
                are_we_in_marker = True
                position_in_character_list += 1
        elif are_we_in_marker:
            if characters[position_in_character_list] != ')':
                current_marker += characters[position_in_character_list]
                position_in_character_list += 1
            else:
                are_we_in_marker = False
                split_marker = current_marker.split('x')
                characters_to_repeat = int(split_marker[0])
                repetitions = int(split_marker[1])
                current_marker = ''
                position_in_character_list += 1
                new_string_to_test = "".join(
                    characters[position_in_character_list:position_in_character_list + characters_to_repeat])
                length += repetitions * decompress_version_2(new_string_to_test)
                characters = characters[(position_in_character_list + characters_to_repeat):]
                position_in_character_list = 0
    return length


if __name__ == "__main__":
    our_input = input_only_one_line("../input.txt")
    decompressed_string = decompress_string(our_input)
    decompressed_length = len(decompressed_string)
    print(f"The decompressed length of the input is {decompressed_length}.")
    print("Now it's time to try the decompression v2 algorithm.")
    decompressed_length_v2 = decompress_version_2(our_input)
    print(f"The decompressed length, using the v2 algorithm is {decompressed_length_v2}.")

# Part 1: 110347 is too high
