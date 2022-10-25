"""Solution to AoC 2016 Day 16: Dragon Checksum"""


def flip_bits(bit_string: str) -> str:
    """Take in a string that looks like bits and flips them."""
    flipped = []
    for character in bit_string:
        if character == "0":
            flipped.append('1')
        else:
            flipped.append('0')
    return ''.join(flipped)


def generate_checksum(data_to_check: str) -> str:
    """Take in a bit string and generate the checksum.

    If the length of the checksum is even, run the process again.
    """
    checksum = []
    for index in range(0, len(data_to_check) - 1, 2):
        if data_to_check[index] == data_to_check[index + 1]:
            checksum.append('1')
        else:
            checksum.append('0')
    if len(checksum) % 2 == 0:
        return generate_checksum(''.join(checksum))
    else:
        return ''.join(checksum)


def fill_disk(initial_state: str, fill_length: int) -> str:
    """Build up a string using the problem's rules, up to the fill_length."""
    length_of_string = len(initial_state)
    our_string = initial_state
    while length_of_string < fill_length:
        our_string_reverse = "".join(reversed(our_string))
        suffix = flip_bits(our_string_reverse)
        our_string = our_string + "0" + suffix
        length_of_string = len(our_string)
    return our_string[0:fill_length]
