def get_puzzle_input():
    """ gets file input and stores into a list by lines"""
    file = open('../input.txt')
    return [num for num in file.readlines()]


def get_initial_config(line):
    """ loads unique lengthed numbers into dictionary """
    cache = {}
    for digit in line.split(" "):
        digit = digit.strip()
        cache[len(digit)] = set(digit)

    return cache


def deduce(digit, cache):
    """ given a digit, this compares values in digit's character set to deduce value """
    if  len(digit) == 6:
            if len(set(digit).union(cache[4])) == 6:
                return "9"
            elif len(set(digit).intersection(cache[1])) == 2:
                return "0"
            else:
                return "6"
    if len(digit) == 5:
        if len(set(digit).union(cache[1])) == len(set(digit)):
            return "3"
        elif len(set(digit).union(cache[4])) == 7:
            return "2"
        else:
            return "5"
    else:
        known = {2: "1", 4: "4", 3: "7", 7: "8"}
        return known[len(digit)]


def translate(final, cache):
    return int("".join([deduce(num, cache) for num in final.split(" ")]))


def main():
    puzzle_input = get_puzzle_input()
    return sum(
        translate(final, get_initial_config(calibration))
        for calibration, final in [
            line.strip().split(" | ") for line in puzzle_input
        ]
    )


if __name__ == '__main__':
    print(main())
