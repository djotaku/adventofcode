from . import solution


def test_find_most_common_letters():
    sample_input = solution.input_per_line("part_1_sample_input.txt")
    word_length = len(sample_input[0])
    answer = solution.decrypt_message(sample_input, word_length)
    assert answer == (['e', 'a', 's', 't', 'e', 'r'],
                      ['a', 'd', 'v', 'e', 'n', 't'])
