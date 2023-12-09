import day_09


def test_find_next_number():
    sequence = [0, 3, 6, 9, 12, 15]
    assert day_09.find_next_number(sequence) + sequence[-1] == 18
    sequence = [1, 3, 6, 10, 15, 21]
    assert day_09.find_next_number(sequence) + sequence[-1] == 28


def test_whole_process():
    lines = day_09.input_per_line("../sample_input.txt")
    extrapolated_values = []
    for line in lines:
        list_seq = day_09.sequence_to_list(line)
        final_number = list_seq[-1]
        add = day_09.find_next_number(list_seq)
        extrapolated_values.append(add + final_number)
    assert sum(extrapolated_values) == 114


def test_find_prior_number_seq_1():
    sequence = [0, 3, 6, 9, 12, 15]
    assert day_09.find_prior_number(sequence) == -3


# def test_find_prior_number_seq_2():
#     sequence = [1, 3, 6, 10, 15, 21]
#     assert day_09.find_prior_number(sequence) == 0


def test_find_prior_number_seq_3():
    sequence = [10, 13, 16, 21, 30, 45]
    assert day_09.find_prior_number(sequence) == 5


def test_part_two():
    lines = day_09.input_per_line("../sample_input.txt")
    extrapolated_values = []
    for line in lines:
        list_seq = day_09.sequence_to_list(line)
        first_number = list_seq[0]
        add = day_09.find_prior_number(list_seq)
        extrapolated_values.append(first_number - add)
    assert sum(extrapolated_values) == 2
