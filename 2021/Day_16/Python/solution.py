"""Solution for Day 16: Packet Decoder"""

import logging
logger_16 = logging.getLogger("Day_16")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()


hex_binary_dictionary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


def hex_to_binary(hexidcecimal_number: str) -> str:
    """Convert this hex number into binary based on our translation instructions.

    see hex_binary_dictionary

    Because each digit becomes 4 binary digits, but later we have to deal with them in 3s and so on, will
    turn it back into a string.
    """
    binary_characters = [hex_binary_dictionary[character] for character in hexidcecimal_number]
    return "".join(binary_characters)


def read_subpacket(subpacket: str) -> dict:
    """Read in a subpacket and return a dictionary of values in that subpacket.

    For part 1 we only care about subpacket version.
    """
    subpacket_broken_up = [character for character in subpacket]
    version = "".join(subpacket_broken_up[0:3])
    packet_type_id = "".join(subpacket_broken_up[3:6])
    logger_16.debug(f"{version=}")
    subpacket_fields = {"version": int(version, 2),
                        "packet_type": int(packet_type_id, 2)}
    if subpacket_fields["version"] == 6:
        # here need to go through the packet and figure out how long it is
        number_of_quintets = 0
        literal_list = []
        for number in range(0, 100, 5):
            number_of_quintets += 1
            this_quintet = subpacket_broken_up[6+number:11+number]
            print(this_quintet)
            quartet = "".join(this_quintet[1:])
            literal_list.append(quartet)
            if this_quintet[0] == "0":
                break
        # may as well also put the number into a field for possibility for part 2
        subpacket_length = 6 + number_of_quintets * 5
        literal_number = int("".join(literal_list), 2)
        print(f"{literal_number=}")
        subpacket_fields["length"] = subpacket_length
        subpacket_fields["literal number"] = literal_number
        return subpacket_fields
    else:
        length_type = subpacket_broken_up[6]
        subpacket_fields["length type"] = length_type
        if length_type == "0":
            length = "".join(subpacket_broken_up[7:22])
            length_of_subpackets = int(length, 2)
            subpacket_list = []
            offset = 0
            while length_of_subpackets > 0:
                this_subpacket = read_subpacket("".join(subpacket_broken_up[23+offset:]))
                subpacket_list.append(this_subpacket)
                length_of_subpackets -= this_subpacket["length"]
                offset += length_of_subpackets
            # for/while loop until run out o length - add subpackets into field "subpacket"
            # add them by calling this method recursively
            # when each subpacket returns, check the length of the subpacket and subtract
            # that from length_of_subpackets. When that gets to 0, we're done searching for
            # subpackets
        elif length_type == "1":
            # figure out how many subpackets we have.
            # As you find each, add to "subpacket" field
            # subtract 1 until at zero
            pass
    return subpacket_fields

# For part 1:
# Parse dict - searching each packet for subpackets and so on - adding up version fields
