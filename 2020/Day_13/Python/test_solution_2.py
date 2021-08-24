from . import solution_2


def test_grab_timetable():
    assert solution_2.grab_timetable('ref_input') == [7, 13, 'x', 'x', 59, 'x', 31, 19]


def test_find_timestamp():
    timetable = [7, 13, 'x', 'x', 59, 'x', 31, 19]
    assert solution_2.find_timestamp(timetable) == 1068781


def test_answer_calculation():
    assert solution_2.answer_calculation(939, (59,944)) == 295
