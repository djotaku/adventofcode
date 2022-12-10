"""Solution to AoC 2022 Day 10 - Cathode-Ray Tube"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def program_execution(assembly: list) -> list:
    """Take in list of assembly code and return list of signal strengths."""
    signal_strengths = []
    register_x = 1
    cycle = 0
    for assembly_code in assembly:
        match assembly_code:
            case "noop":
                cycle += 1
            case _:
                cycle += 1
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    print(f"{cycle=}")
                    print(f"{register_x=}")
                    signal_strengths.append(register_x * cycle)
                command = assembly_code.split()
                register_x += int(command[1])
                cycle += 1
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            print(f"{cycle=}")
            print(f"{register_x=}")
            signal_strengths.append(register_x * cycle)
    return signal_strengths


if __name__ == "__main__":
    code_to_execute = input_per_line("../complex_sample_input.txt")
    executed_signal_strengths = program_execution(code_to_execute)
    print(f"{executed_signal_strengths}")
