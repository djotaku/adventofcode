from . import solution_2


def test_parse_input():
    rules = ['class: 0-1 or 4-19\n', 'row: 0-5 or 8-19\n', 'seat: 0-13 or 16-19\n']
    your_ticket = '11,12,13\n'
    nearby_tickets = ['3,9,18', '15,1,5', '5,14,9']
    assert solution_2.parse_input('ref_input_2') == (rules, your_ticket, nearby_tickets)


def test_create_rule_dictionary():
    rule_dictionary = solution_2.create_rule_dictionary(['class: 0-1 or 4-19\n', 'row: 0-5 or 8-19\n',
                                                         'seat: 0-13 or 16-19\n'])
    assert rule_dictionary['class'] == {0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}


def test_keep_valid_tickets():
    rules, your_ticket, nearby_tickets = solution_2.parse_input('ref_input')
    rule_dictionary = solution_2.create_rule_dictionary(rules)
    assert solution_2.keep_valid_tickets(rule_dictionary, nearby_tickets) == ['7,3,47']


def test_figure_out_fields():
    rule_dictionary = solution_2.create_rule_dictionary(['class: 0-1 or 4-19\n', 'row: 0-5 or 8-19\n',
                                                         'seat: 0-13 or 16-19\n'])
    valid_tickets = ['3,9,18', '15,1,5', '5,14,9']
    assert solution_2.figure_out_fields(rule_dictionary, valid_tickets) == ['row', 'class', 'seat']
