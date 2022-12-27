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


def find_even_division(row:str) -> int:
    """Take in a row and find the two numbers that evenly divide. Return the result of that division."""
    nums = row.split()
    nums = [int(number) for number in nums]
    row_length = len(nums)
    for num in nums:
        for index in range(row_length):
            if num % nums[index] == 0 and num != nums[index]:
                return num // nums[index]

if __name__ == "__main__":
    debug = False
    if debug:
        input_file = "../sample_input.txt"
    else:
        input_file = "../input.txt"
    spreadsheet = input_per_line(input_file)
    rows = [row_difference(row) for row in spreadsheet]
    print(f"The checksum is {sum(rows)}.")
    row_modulo = [find_even_division(row) for row in spreadsheet]
    print(row_modulo)
    print(f"The checksum is actually {sum(row_modulo)}.")