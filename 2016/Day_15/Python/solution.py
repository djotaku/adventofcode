"""Solution for AoC 2016 Day 15: Timing is Everything"""
import math


def find_capsule_time(discs: list) -> int:
    """Figure out what time to start the machine.

    discs list should contain tuples: (positions, starting position)

    Order matters, it should be the order of discs in the machine.
    """
    # reaches the first disc at t=1.
    # first figure out the time points where each disc gets to 0 the first time
    disc_first_zero = []
    for time, disc in enumerate(discs, start=1):
        distance_from_hole = (time + disc[1]) % disc[0]
        if distance_from_hole == 0:
            disc_first_zero.append(time)
        else:
            disc_first_zero.append(time+distance_from_hole)
    # figure out the time that works for all the values in disc_first_zero
    # LCM?
    print(disc_first_zero)
    return math.lcm(*disc_first_zero)


if __name__ == "__main__":
    pass
