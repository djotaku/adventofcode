"""Solution to AoC Day 04 - Camp Cleanup"""
def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def contained_pairs(pair: str) -> int:
    """Figure out if one pair fully contains the other."""
    elf_one = set()
    elf_two = set()
    elf_one_list, elf_two_list = pair.split(",")
    elf_one_start, elf_one_end = elf_one_list.split("-")
    elf_two_start, elf_two_end = elf_two_list.split("-")
    for number in range(int(elf_one_start), int(elf_one_end)+1):
        elf_one.add(number)
    for number in range(int(elf_two_start), int(elf_two_end)+1):
        elf_two.add(number)
    if elf_one.issubset(elf_two) or elf_two.issubset(elf_one):
        return 1
    else: return 0


def check_partial_overlap(pair: str) -> int:
    """Use isdisjoint and return 1 if it's false."""
    elf_one = set()
    elf_two = set()
    elf_one_list, elf_two_list = pair.split(",")
    elf_one_start, elf_one_end = elf_one_list.split("-")
    elf_two_start, elf_two_end = elf_two_list.split("-")
    for number in range(int(elf_one_start), int(elf_one_end) + 1):
        elf_one.add(number)
    for number in range(int(elf_two_start), int(elf_two_end) + 1):
        elf_two.add(number)
    if elf_one.isdisjoint(elf_two):
        return 0
    else:
        return 1

if __name__ == "__main__":
    cleanup_sections = input_per_line("../input.txt")
    pairs = [contained_pairs(section) for section in cleanup_sections]
    print(f"There are {sum(pairs)} fully contained assignment pairs.")
    any_overlap = [check_partial_overlap(section) for section in cleanup_sections]
    print(f"There are {sum(any_overlap)} pairs with any overlap at all.")