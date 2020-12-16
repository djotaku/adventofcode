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

########################
# old tests

#def test_find_invalid_numbers():
#    set_to_test_against = {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 13, 14, 15,
#                           16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 45, 46, 47, 48, 49, 50}
#    assert solution_2.find_invalid_numbers(['7,3,47', '40,4,50', '55,2,20', '38,6,12'], set_to_test_against) == [4, 55,
#                                                                                                                 12]


#def test_find_error_rate():
#    assert solution_2.find_error_rate([4, 55, 12]) == 71
