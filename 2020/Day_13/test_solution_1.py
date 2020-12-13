from . import solution_1


def test_grab_timetable():
    assert solution_1.grab_timetable('ref_input') == (939, [7, 13, 'x', 'x', 59, 'x', 31, 19])


def test_find_earliest_bus_id_timestamp():
    timetable = (939, [7, 13, 'x', 'x', 59, 'x', 31, 19])
    assert solution_1.find_earliest_bus_id_timestamp(timetable) == (59, 944)