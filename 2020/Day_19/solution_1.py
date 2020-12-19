def parse_rules(input_file):
    with open(input_file, 'r') as file:
        rules_dictionary = dict()
        rules_input = [line.rstrip() for line in file.readlines() if line != '\n' and line[0].isdigit()]
        for rule in rules_input:
            temp_rule = rule.split(':')
            if temp_rule[1].__contains__('a') or temp_rule[1].__contains__('b'):
                rules_dictionary[temp_rule[0]] = temp_rule[1]
            if temp_rule[1].__contains__('|'):
                temp_2 = temp_rule[1].split('|')
                temp_2[0] = temp_2[0].split()
                temp_2[1] = temp_2[1].split()
                rules_dictionary[temp_rule[0]] = temp_2
            else:
                rules_dictionary[temp_rule[0]] = temp_rule[1].split()
    return rules_dictionary


def regular_expression_combinations(rules_dictionary):
    combinations = []
    for item in rules_dictionary['0']:
        if len(rules_dictionary[item]) == 1:
            combinations.append(rules_dictionary[item[0]]) #.lstrip('"').rstrip('"'))
    return combinations