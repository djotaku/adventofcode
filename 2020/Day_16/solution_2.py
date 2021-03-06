import re


class TicketField:
    def __init__(self, name, non_locations):
        self.name = name
        self.non_locations = non_locations

    def __gt__(self, other):
        return len(self.non_locations) < len(other.non_locations)

    def __repr__(self):
        return f"Ticket called {self.name} with {self.non_locations}"


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
    # print(set_to_test_against)
    for ticket in nearby_tickets:
        numbers = ticket.split(',')
        for number in numbers:
            if int(number) not in set_to_test_against:
                invalid_tickets.append(ticket)
                break
        if ticket not in invalid_tickets:
            valid_tickets.append(ticket)
    return valid_tickets


def determine_number(possibility_space, do_not_put_me_here):
    return set(possibility_space) - set(do_not_put_me_here)


def figure_out_fields(rule_dictionary, valid_tickets):
    dictionary_of_not_locations = dict()
    for ticket in valid_tickets:
        numbers = ticket.split(',')
        for index in range(0, len(numbers)):
            for key, value in rule_dictionary.items():
                if int(numbers[index]) not in value:
                    if key not in dictionary_of_not_locations:
                        dictionary_of_not_locations[key] = [index]
                    else:
                        dictionary_of_not_locations[key] += [index]
    a_ticket = valid_tickets[0].split(',')
    field_length = len(a_ticket)
    possibility_field = [number for number in range(0, field_length)]
    # print(possibility_field)
    # print(dictionary_of_not_locations)
    ticket_fields = []
    for key, value in dictionary_of_not_locations.items():
        ticket_fields.append(TicketField(key, value))
    return_order = [0] * len(rule_dictionary)
    for field in sorted(ticket_fields):
        position = determine_number(possibility_field, field.non_locations).pop()
        return_order[position] = field.name
        possibility_field.remove(position)
    last_field = (set(rule_dictionary.keys()) - set(return_order)).pop()
    return_order[possibility_field.pop()] = last_field
    return return_order


def get_your_ticket_indexes(fields):
    return [fields.index(field) for field in fields if re.search(r'departure', field)]


if __name__ == "__main__":
    rules, your_ticket, nearby_tickets = parse_input('input')
    rules_dictionary = create_rule_dictionary(rules)
    valid_tickets = keep_valid_tickets(rules_dictionary, nearby_tickets)
    fields_in_order = figure_out_fields(rules_dictionary, valid_tickets)
    print(fields_in_order)
    ticket_indexes = get_your_ticket_indexes(fields_in_order)
    print(ticket_indexes)
    ticket_stage_1 = your_ticket.rstrip()
    ticket_list = ticket_stage_1.split(',')
    multiply_me = [ticket_list[item] for item in ticket_indexes]
    print(multiply_me)
    product = 1
    for number in multiply_me:
        product *= int(number)
    print(f'The answer is {product}')