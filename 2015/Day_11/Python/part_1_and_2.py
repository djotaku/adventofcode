import re


def rule_one(password: str) -> bool:
    """Check if a password includes a straight of at least 3 letters."""
    for index, letter in enumerate(password):
        if index == (len(password) - 3):
            return False
        current_letter_ascii_value = ord(letter)
        if ord(password[index + 1]) == current_letter_ascii_value + 1 and\
                ord(password[index + 2]) == current_letter_ascii_value + 2:
            return True


def rule_two(password: str) -> bool:
    """Check if a password contains i, o, or l."""
    return 'i' not in password and 'o' not in password and 'l' not in password


def rule_three(password: str) -> bool:
    """Check for at least two different, non-overlapping pairs of letters."""
    rule_three_regex = re.compile(r'(\w)\1')
    all_pairs = re.findall(rule_three_regex, password)
    if len(all_pairs) < 2:
        return False
    if len(set(all_pairs)) > 1:
        return True


def increment_password(password: str) -> str:
    """Given a password, increment the last letter by 1."""
    if password[-1] == 'z':
        return increment_password(password[:-1]) + 'a'
    return password[:-1] + chr(ord(password[-1]) + 1)


def find_next_valid_password(password: str) -> str:
    """Find the next password that meets all the criteria"""
    while True:
        if rule_one(password) and rule_two(password) and rule_three(password):
            return password
        password = increment_password(password)


puzzle_input = "hxbxwxba"
first_new_password = find_next_valid_password(puzzle_input)
second_new_password = find_next_valid_password(increment_password(first_new_password))
print(f"Santa's first new password is {first_new_password}")
print(f"Santa's second new password is {second_new_password}")
