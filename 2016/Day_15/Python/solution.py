"""Solution for AoC 2016 Day 15: Timing is Everything"""
import math


def find_capsule_time(discs: list) -> int:
    """Figure out what time to start the machine.

    discs list should contain tuples: (positions, starting position)

    Order matters, it should be the order of discs in the machine.
    """
    # reaches the first disc at t=1.
    # first figure out the time points where each disc gets to 0 the first time
    time = 0
    loop = True
    drop_check = []
    while loop:
        time += 1
        for time_delta, disc in enumerate(discs, start=1):
            if (disc[1] + time + time_delta) % disc[0] == 0:
                drop_check.append(True)
            else:
                drop_check.append(False)
        if all(drop_check):
            loop = False
        drop_check.clear()
    return time


if __name__ == "__main__":
    pass
