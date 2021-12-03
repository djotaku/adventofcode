"""Solution for 2021 Day 03: Binary Diagnostic"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def binary_positions(diagnostics: list) -> int:
    """Take in a list of binary numbers. Add up the number of 1s in each position.

    Compare this to half the length of diagnostics to see if it's the majority.

    Convert binary number to decimal. (gamma rate)

    Bit invert the number and convert that to decimal. (epsilon rate)

    Multiply and return.
    """
    diagnostics_length = len(diagnostics)
    gamma_rate = ""
    epsilon_rate = ""
    position_count_dict = {}
    for diagnostic_line in diagnostics:
        positional_diagnostic = [int(pos) for pos in diagnostic_line]
        for index, position_value in enumerate(positional_diagnostic):
            if index in position_count_dict:
                position_count_dict[index] += position_value
            else:
                position_count_dict[index] = position_value
    for key, value in position_count_dict.items():
        if value > diagnostics_length/2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    gamma_rate_binary = bytearray(gamma_rate, "utf8")
    epsilon_rate_binary = bytearray(epsilon_rate, "utf8")
    gamma_rate_decimal = int(gamma_rate_binary, 2)
    epsilon_rate_decimal = int(epsilon_rate_binary, 2)
    return gamma_rate_decimal * epsilon_rate_decimal


if __name__ == "__main__":
    our_diagnostics = input_per_line("../input.txt")
    part_one = binary_positions(our_diagnostics)
    print(f"Our power consumption is {part_one}.")