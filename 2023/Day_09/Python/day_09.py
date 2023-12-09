"""Solution to AoC 2023 Day 09: Mirage Maintenance."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_next_number(sequence: list[int]) -> int:
    """Figure out the next number in the sequence using puzzle's algorithm."""
    if all(v == 0 for v in sequence):
        print(f"I am all 0s? {sequence=}")
        return 0
    else:
        this_sequence = [
            sequence[num + 1] - sequence[num]
            for num in range(len(sequence) - 1)
        ]
        print(f"{this_sequence=}")
        print(f"{this_sequence[-1]}")
        return this_sequence[-1] + find_next_number(this_sequence)


def sequence_to_list(sequence: str) -> list[int]:
    """Take in the sequence from the input and turn it into a list of ints."""
    sequence_numbers = sequence.split()
    return [int(number) for number in sequence_numbers]


if __name__ == '__main__':
    histories = input_per_line("../input.txt")
    extrapolated_values = []
    for line in histories:
        list_seq = sequence_to_list(line)
        final_number = list_seq[-1]
        add = find_next_number(list_seq)
        extrapolated_values.append(add + final_number)
    print(f"The sum of extrapolated values is {sum(extrapolated_values)}")