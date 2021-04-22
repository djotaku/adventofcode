from datetime import datetime
from functools import lru_cache
import re
import sys
sys.path.insert(0, '../../input_parsing')
import parse_input

all_wires = {}


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


def break_up_equation(equation):
    """Figure out the operand(s) and operation and return them."""
    two_operand_regex = re.compile(r'(\w+) ([A-Z]*) (\w+)')
    one_operand_regex = re.compile('([A-Z]*) ([a-z]+)')
    if re.match(two_operand_regex, equation):
        result = re.findall(two_operand_regex, equation)
        return result[0][0], result[0][1], result[0][2]
    elif re.match(one_operand_regex, equation):
        result = re.findall(one_operand_regex, equation)
        return result[0][0], result[0][1]
    else:
        return [equation]


@lru_cache()
def find_value_on_line(wire_to_find):
    """Figure out what the final value is on a wire."""
    if all_wires[wire_to_find].isnumeric():
        return int(all_wires[wire_to_find])
    equation = break_up_equation(all_wires[wire_to_find])
    if len(equation) == 3:
        if equation[0].isnumeric():
            operand_left = int(equation[0])
        else:
            operand_left = find_value_on_line(equation[0])
        if equation[2].isnumeric():
            operand_right = int(equation[2])
        else:
            operand_right = find_value_on_line(equation[2])
        operation = equation[1]
        if operation == "AND":
            return operand_left & operand_right
        elif operation == "LSHIFT":
            return operand_left << operand_right
        elif operation == "OR":
            return operand_left | operand_right
        elif operation == "RSHIFT":
            return operand_left >> operand_right
    elif len(equation) == 2:
        return find_value_on_line(equation[1]) ^ 65535
    else:
        return find_value_on_line(equation[0])


if __name__ == "__main__":
    print(f"Starting at {datetime.now().strftime('%d-%b-%Y %H:%M:%S')}")
    bobby_instructions = parse_input.input_per_line('../input.txt')
    all_wires = create_dictionary(bobby_instructions)
    all_wires['b'] = "956"
    wire_a = find_value_on_line('a')
    print(f"The value on wire a is {wire_a}")
    print(f"Ended at {datetime.now().strftime('%d-%b-%Y %H:%M:%S')}")

# the answer is not -7074
# 58462 is too high