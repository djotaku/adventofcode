# Solution to AoC 2024 Day 02: Red-Nosed Reports

from copy import deepcopy

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def check_same_direction(numbers: list[int]) -> bool:
    """Check whether the numbers are all increasing or all decreasing and return true if they are.
    This function will return True if there's a delta 0 between 2 numbers, but that will be caught in delta check."""
    sorted_numbers = sorted(numbers)
    reverse_sorted_numbers = sorted(numbers, reverse=True)
    for (a, b) in zip(numbers, numbers[1:]):
        if a == b:
            return False
    return True if sorted_numbers == numbers else reverse_sorted_numbers == numbers


def apply_dampener_to_same_direction(numbers: list[int]) -> (bool, list[int]):
    """Keeps checking if removing one number would fix the same direction error."""
    checks = len(numbers)
    if check_same_direction(numbers): # would have passed anyway
        return True, numbers
    for position in range(checks):
        modified_numbers = [
            number for pos, number in enumerate(numbers) if pos != position
        ]
        if check_same_direction(modified_numbers):
            return True, modified_numbers
    return False, numbers

def apply_dampener_to_check_delta(numbers: list[int]) -> (bool, list[int]):
    """Keeps checking if removing one number would fix the same delta error."""
    checks = len(numbers)
    if check_delta(numbers): # would have passed anyway
        return True, numbers
    for position in range(checks):
        modified_numbers = [
            number for pos, number in enumerate(numbers) if pos != position
        ]
        if check_delta(modified_numbers):
            return True, modified_numbers
    return False, numbers

def check_delta(numbers: list[int])->bool:
    """Check whether the delta between any 2 numbers is between 1-3 inclusive."""
    deltas = []
    for (a,b) in zip(numbers, numbers[1:]):
        if abs(a-b) in [1,2,3]:
            deltas.append(True)
        else:
            deltas.append(False)
    return all(deltas)

def dampener(numbers: list[int])->bool:
    (worked, new_list) = apply_dampener_to_same_direction(numbers)
    if worked and check_delta(new_list):
        return True
    (worked, new_list) = apply_dampener_to_check_delta(numbers)
    if  worked and check_same_direction(new_list):
            return True
    return False

if __name__ == '__main__':
    our_input = input_per_line("../input.txt")
    safe_rows = 0
    for row in our_input:
        split_row = row.split()
        split_row = [int(value) for value in split_row]
        if check_same_direction(split_row) and check_delta(split_row):
            safe_rows+=1
    print(f"there are {safe_rows} safe reports.")
    print("Applying dampener.....")
    safe_dampened_rows = 0
    for row in our_input:
        split_row = row.split()
        split_row = [int(value) for value in split_row]
        if dampener(split_row):
                safe_dampened_rows += 1
    print(f"there are {safe_dampened_rows} safe reports with the dampener applied.")

# 564 is too low