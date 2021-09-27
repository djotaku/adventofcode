from collections import defaultdict


def while_loop_answer(bus_table_list, departure_time_for_first_bus):
    for bus_index, bus in enumerate(bus_table_list):
        if (
                bus != "x"
                and (departure_time_for_first_bus + bus_index) % int(bus) != 0
        ):
            return False
    return True


def buses_in_a_row(bus_table_list, departure_time_for_first_bus):
    answer = 0
    for bus_index, bus in enumerate(bus_table_list):
        if (
                bus != "x"
                and (departure_time_for_first_bus + bus_index) % int(bus) != 0
        ):
            return answer
        if bus != "x":
            answer += 1


def determine_interval(bus_table_list, departure_time_for_first_bus, interval_dictionary, interval):
    how_many_busses_in_a_row = buses_in_a_row(bus_table_list, departure_time_for_first_bus)

    if how_many_busses_in_a_row == 0:
        return interval

    interval_dictionary[how_many_busses_in_a_row].append(departure_time_for_first_bus)

    if len(interval_dictionary[how_many_busses_in_a_row]) > 1:
        proposed_interval = interval_dictionary[how_many_busses_in_a_row][-1] - interval_dictionary[how_many_busses_in_a_row][-2]
        interval = max(proposed_interval, interval)
    return  interval

def find_consecutive_leave_time(bus_table: str, testing: bool = False) -> int:
    """Find the time at which each bus leaves one minute after the bus before it."""
    bus_table_list = bus_table.split(',')
    departure_time_for_first_bus = 0 if testing else 100000000000000
    interval = 1
    interval_dictionary = defaultdict(list)
    while not while_loop_answer(bus_table_list, departure_time_for_first_bus):
        interval = determine_interval(bus_table_list, departure_time_for_first_bus, interval_dictionary, interval)
        departure_time_for_first_bus += interval
    return departure_time_for_first_bus


if __name__ == "__main__":
    bus_table = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
    leave_time = find_consecutive_leave_time(bus_table)
    print(leave_time)
