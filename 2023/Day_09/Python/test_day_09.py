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
