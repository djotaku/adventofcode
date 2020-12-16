import re


def parse_input(input_file):
    with open(input_file, 'r') as file:
        inputs = file.readlines()
        rules = []
        for line in inputs:
            if line != '\n':
                rules.append(line)
            elif line == '\n':
                break
        where_is_your_ticket = inputs.index('your ticket:\n')
        your_tickets = inputs[where_is_your_ticket+1]
        where_is_nearby_tickets = inputs.index('nearby tickets:\n')
        nearby_tickets = []
        for index in range(where_is_nearby_tickets + 1, len(inputs)):
            nearby_tickets.append(inputs[index].rstrip())
    return rules, your_tickets, nearby_tickets


def create_rule_dictionary(rules):
    dictionary_to_return = dict()
    set_of_values = set()
    for rule in rules:
        split_key_and_value = rule.split(':')
        break_up_values = split_key_and_value[1].split('or')
        for value in break_up_values:
            range_numbers = re.findall(r'\d+', value)
            for number in range(int(range_numbers[0]), int(range_numbers[1])+1):
                set_of_values.add(number)
        dictionary_to_return[split_key_and_value[0]] = set_of_values.copy()
        set_of_values.clear()
    return dictionary_to_return


def keep_valid_tickets(rule_dictionary, nearby_tickets):
    set_to_test_against = set()
    valid_tickets = []
    invalid_tickets = []
    for value in rule_dictionary.values():
        set_to_test_against |= value
    print(set_to_test_against)
    for ticket in nearby_tickets:
        numbers = ticket.split(',')
        for number in numbers:
            if int(number) not in set_to_test_against:
                invalid_tickets.append(ticket)
                break
        if ticket not in invalid_tickets:
            valid_tickets.append(ticket)
    return valid_tickets


def figure_out_fields(rule_dictionary, valid_tickets):
    dictionary_of_possibilities = dict()
    for ticket in valid_tickets:
        numbers = ticket.split(',')
        for index in range(0, len(numbers)):
            for key, value in rule_dictionary.items():
                temp_list = []
                if int(numbers[index]) in value:
                    temp_list.append(key)
                if index not in dictionary_of_possibilities:
                    dictionary_of_possibilities[index] = temp_list.copy()
                else:
                    current = dictionary_of_possibilities[index]
                    dictionary_of_possibilities[index] = current + temp_list.copy()
    print(*dictionary_of_possibilities.values())
    return None


def find_error_rate(invalid_numbers):
    return sum(invalid_numbers)


if __name__ == "__main__":
    our_input = parse_input('input')
    set_of_valid_numbers = build_set(our_input[0])
    invalid_numbers = find_invalid_numbers(our_input[1], set_of_valid_numbers)
    print(f'The answer is {find_error_rate(invalid_numbers)}')