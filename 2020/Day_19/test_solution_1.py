from . import solution_1


def test_parse_rules():
    rules_dictionary = solution_1.parse_rules('ref_rules')
    assert rules_dictionary['0'] == ['4', '1', '5']
    assert rules_dictionary['1'] == [['2', '3'], ['3', '2']]
    assert rules_dictionary['2'] == [['4', '4'], ['5', '5']]
    assert rules_dictionary['3'] == [['4', '5'], ['5', '4']]
    assert rules_dictionary['4'] == 'a'
    assert rules_dictionary['5'] == 'b'


def test_regular_expression_combinations():
    rules_dictionary = solution_1.parse_rules('ref_rules')
    assert solution_1.regular_expression_combinations(rules_dictionary) == ['aaaabb', 'aaabab', 'abbabb', 'abbbab',
                                                                            'aabaab', 'aabbbb', 'abaaab', 'ababbb']
