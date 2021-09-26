def find_consecutive_leave_time(bus_table_list: list, departure_time, interval) -> int:
    """Find the time at which each bus leaves one minute after the bus before it."""
    # departure_time_for_first_bus = 0 if testing else 100000000000000
    departure_time_for_first_bus = departure_time
    seek_departure_time = False
    while not seek_departure_time:
        departure_time_for_first_bus += interval
        seek_departure_time = all(((departure_time_for_first_bus + bus[0]) % bus[1] == 0) for bus in bus_table_list)
    return departure_time_for_first_bus


def create_useful_bus_list(bus_table: str):
    bus_table_list = bus_table.split(',')
    return [
        (bus_index, int(bus))
        for bus_index, bus in enumerate(bus_table_list)
        if bus != 'x'
    ]


def solve_two_busses_at_a_time(bus_table_list: list):
    solution = 0
    interval = bus_table_list[0][1]
    while bus_table_list:
        print(f"{bus_table_list=}")
        position_for_next_go = bus_table_list[1][0]
        print(f"{position_for_next_go=}")
        solution = find_consecutive_leave_time([bus_table_list.pop(0), bus_table_list.pop(0)], 0, interval)
        print(f"{solution=}")
        if bus_table_list:
            bus_table_list.insert(0, (0, solution))
    return solution


if __name__ == "__main__":
    bus_table = "7,13,x,x,59,x,31,19"
    #bus_table = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
    bus_table_list = create_useful_bus_list(bus_table)
    print(solve_two_busses_at_a_time(bus_table_list))
    #leave_time = find_consecutive_leave_time(bus_table_list, True)
    #print(leave_time)
