"""Solution to AoC 2017 Day 2 - Corruption Checksum."""

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def row_difference(row: str) -> int:
    """Take in a row and calculate the difference between the largest and smallest number. Return it."""
    nums = row.split()
    nums = [int(number) for number in nums]
    return max(nums) - min(nums)

if __name__ == "__main__":
    spreadsheet = input_per_line("../input.txt")
    rows = [row_difference(row) for row in spreadsheet]
    print(f"The checksum is {sum(rows)}.")