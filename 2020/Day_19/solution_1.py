def parse_rules(input_file):
    with open(input_file, 'r') as file:
        rules_dictionary = dict()
        temp_rule = []
        rules_input = [line.rstrip() for line in file.readlines() if line != '\n' and line[0].isdigit()]
        for rule in rules_input:
            temp_rule.append(rule.split(':'))
        rules_dictionary = dict(temp_rule)
        for key, value in rules_dictionary.items():
            if value == ' "a"' or value == ' "b"':
                rules_dictionary[key] = value.lstrip(' "').rstrip('"')
            elif value.__contains__('|'):
                temp_value = value.split('|')
                temp_value[0] = temp_value[0].split()
                temp_value[1] = temp_value[1].split()
                rules_dictionary[key] = temp_value
            else:
                rules_dictionary[key] = value.split()

    return rules_dictionary


def regular_expression_combinations(rules_dictionary):
    combinations = []
    for item in rules_dictionary['0']:
        if len(rules_dictionary[item]) == 1:
            combinations.append(rules_dictionary[item[0]])
    return combinations