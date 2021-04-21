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


def break_up_equation(equation):
    """Figure out the operand(s) and operation and return them."""
    two_operand_regex = re.compile(r'([a-z]+) ([A-Z]*) (\w)')
    one_operand_regex = re.compile('([A-Z]*) ([a-z]+)')
    if re.match(two_operand_regex, equation):
        result = re.findall(two_operand_regex, equation)
        return result[0][0], result[0][1], result[0][2]
    else:
        result = re.findall(one_operand_regex, equation)
        return result[0][0], result[0][1]


def find_value_on_line(all_wires, wire_to_find):
    """Figure out what the final value is on a wire."""
    if all_wires[wire_to_find].isnumeric():
        return int(all_wires[wire_to_find])
    else:
        equation = break_up_equation(all_wires[wire_to_find])
        if len(equation) == 3:
            operand_left = find_value_on_line(all_wires, equation[0])
            operand_right = find_value_on_line(all_wires, equation[2])
            operation = equation[1]
            if operation == "AND":
                return operand_left & operand_right
            elif operation == "LSHIFT":
                return operand_left << operand_right
            elif operation == "OR":
                return operand_left | operand_right
            elif operation == "RSHIFT":
                return operand_left >> operand_right
        else:
            return ~ find_value_on_line(all_wires, equation[1])