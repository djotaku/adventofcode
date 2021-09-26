import part_2


def test_find_consecutive_leave_time():
    bus_table = part_2.create_useful_bus_list("7,13,x,x,59,x,31,19")
    leave_time = part_2.find_consecutive_leave_time(bus_table, 0, 7)
    assert leave_time == 1068781
    bus_table = part_2.create_useful_bus_list("17,x,13,19")
    leave_time = part_2.solve_two_busses_at_a_time(bus_table)
    #leave_time = part_2.find_consecutive_leave_time(bus_table, True)
    assert leave_time == 3417
    #bus_table = "67,7,59,61"
    #leave_time = part_2.find_consecutive_leave_time(bus_table, True)
    #assert leave_time == 754018
