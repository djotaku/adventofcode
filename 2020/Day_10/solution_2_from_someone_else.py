from collections import Counter

def import_joltages(input_file):
    with open(input_file, 'r') as file:
        return [int(line) for line in file.readlines()]


if __name__ == "__main__":
    joltage_list = sorted(import_joltages('input') + [0])
    print(joltage_list)
    c = Counter({0: 1})
    for adapter in joltage_list:
        c[adapter + 1] += c[adapter]
        c[adapter + 2] += c[adapter]
        c[adapter + 3] += c[adapter]

    print(f"And the answer is {c[max(joltage_list)+3]}")

"""
Explanation of the algorithm from another who replied they basically did the same thing:

    To find a solution, imagine that you have 5 adapters with outputs of [1, 2, 3, 4, 5] jolts
     and a wall socket with 0 jolts output.
    To connect 1-jolt adapter to the wall according to the rules you have only 1 option - direct connection.
    To connect 2-jolt adapter to the wall you have 2 options - 1-jolt adapter or a direct connection.
    To connect 3-jolt adapter to the wall you have 4 options - 2 ways to connect through 2-jolt adapter,
     1 way through 1-jolt adapter or a direct connection.
    To connect 4-jolt adapter your choice is only through 3-, 2-, or 1- jolt adapters.
    Direct connection has incorrect input parameters.
    That means that you have 4 + 2 + 1 options to connect 4 jolt adapter to the wall.
    The same with 5-jolt adapter - only through 4-, 3-, 2- adapters, and so on and so on.

    If your personal input doesn't have some specific adapters - that's okay,
     that means you just have zero options of connecting through them.
    According to the rules you always will have at least one of 3 adapters needed anyway.

    Written this way the puzzle is pretty straightforward.
    """