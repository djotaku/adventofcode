def find_consecutive_leave_time(bus_table: str, testing: bool = False) -> int:
    """Find the time at which each bus leaves one minute after the bus before it."""
    bus_table_list = bus_table.split(',')
    departure_time_for_first_bus = 1 if testing else 100000000000000
    seek_departure_time = False
    increment = 1
    for bus_index, bus in enumerate(bus_table_list):
        if bus != "x":
            while not seek_departure_time:
                if (departure_time_for_first_bus + bus_index) % int(bus) == 0:
                    increment *= int(bus)
                else:
                    departure_time_for_first_bus += increment
    return departure_time_for_first_bus


if __name__ == "__main__":
    bus_table = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
    leave_time = find_consecutive_leave_time(bus_table)
    print(leave_time)
