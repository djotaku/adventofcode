import re

def parse_input(input_file):
    with open(input_file, 'r') as file:
        inputs = file.readlines()
        rules_level_1 = []
        for line in inputs:
            if line != '\n':
                rules_level_1.append(line)
            elif line == '\n':
                break
        rules = []
        for rule in rules_level_1:
            split = rule.split(':')
            remove_newline = split[1].rstrip('\n')
            remove_space = remove_newline.lstrip()
            rules.append(remove_space)
        where_is_nearby_tickets = inputs.index('nearby tickets:\n')
        nearby_tickets = []
        for index in range(where_is_nearby_tickets + 1, len(inputs)):
            nearby_tickets.append(inputs[index].rstrip())
    return rules, nearby_tickets


def build_set(rule_list):
    set_of_values = set()
    for rule in rule_list:
        break_up_rule = rule.split('or')
        for rule_range in break_up_rule:
            range_numbers = re.findall(r'\d+', rule_range)
            for number in range(int(range_numbers[0]), int(range_numbers[1])+1):
                set_of_values.add(number)
    return set_of_values


def find_invalid_numbers(numbers_to_validate, set_to_test_against):
    invalid_numbers = []
    for number_set in numbers_to_validate:
        numbers = number_set.split(',')
        for number in numbers:
            if int(number) not in set_to_test_against:
                invalid_numbers.append(int(number))
    return invalid_numbers


def find_error_rate(invalid_numbers):
    return sum(invalid_numbers)


if __name__ == "__main__":
    our_input = parse_input('input')
    set_of_valid_numbers = build_set(our_input[0])
    invalid_numbers = find_invalid_numbers(our_input[1], set_of_valid_numbers)
    print(f'The answer is {find_error_rate(invalid_numbers)}')
