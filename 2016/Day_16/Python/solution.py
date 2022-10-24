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
