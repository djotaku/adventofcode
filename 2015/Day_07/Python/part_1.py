import re


def create_dictionary(instructions):
    """Take in instructions and place the connections into a dictionary entry for the wire.
    eg: 123 -> x would lead to a key of x and a value of 123.
    """
    wires = {}
    for instruction in instructions:
        pattern = re.compile(r'(.*) -> (\w+)')
        regex = re.findall(pattern, instruction)
        connection = regex[0][0]
        wire = regex[0][1]
        wires[wire] = connection
    return wires


def find_value_on_line(all_wires, wire_to_find):
    """Figure out what the final value is on a wire."""
    if all_wires[wire_to_find].isnumeric():
        return int(all_wires[wire_to_find])
