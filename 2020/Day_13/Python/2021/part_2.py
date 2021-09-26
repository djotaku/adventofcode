def find_consecutive_leave_time(bus_table: str, testing: bool = False) -> int:
    """Find the time at which each bus leaves one minute after the bus before it."""
    bus_table_list = bus_table.split(',')
    departure_time_for_first_bus = 0 if testing else 100000000000000
    seek_departure_time = False
    while not seek_departure_time:
        departure_time_for_first_bus += int(bus_table_list[0])
        temp_list = []
        for bus_index, bus in enumerate(bus_table_list):
            if bus != "x":
                if (departure_time_for_first_bus + bus_index) % int(bus) == 0:
                    temp_list.append(True)
                else:
                    temp_list.append(False)
        seek_departure_time = all(temp_list)
        temp_list.clear()
    return departure_time_for_first_bus


if __name__ == "__main__":
    bus_table = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,541,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,983,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
    leave_time = find_consecutive_leave_time(bus_table)
    print(leave_time)
