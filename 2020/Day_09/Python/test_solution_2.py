from . import solution_2


def test_find_the_sum():
    input_list = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127]
    assert solution_2.find_the_sum(input_list, 127) == [15, 25, 47, 40]


def test_find_weakness():
    input_list = [15, 25, 47, 40]
    assert solution_2.find_weakness(input_list) == 62


def test_final_answer():
    assert solution_2.final_answer('ref_input', 127) == 62