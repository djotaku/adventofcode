"""Solution for AoC Day 19: An Elephant Named Joseph"""


def game_round(elfs_and_presents: dict) -> (dict, bool):
    """play one round of the white elephant game."""
    elves_still_in_game = [key for key in elfs_and_presents.keys() if elfs_and_presents[key] is True]
    if len(elves_still_in_game) == 1:
        return elfs_and_presents, False
    for index, this_elf in enumerate(elves_still_in_game):
        if elfs_and_presents[this_elf]:
            if this_elf != elves_still_in_game[-1]:
                elfs_and_presents[elves_still_in_game[index+1]] = False
            else:
                elfs_and_presents[elves_still_in_game[0]] = False
    return elfs_and_presents, True


if __name__ == "__main__":
    ELVES = 3018458
    elf_presents = {}
    for elf in range(1, ELVES + 1):
        elf_presents[elf] = True
    continue_game = True
    while continue_game:
        elf_presents, continue_game = game_round(elf_presents)
    for elf, present_bool in elf_presents.items():
        if present_bool is True:
            print(f"The elf with all the presents is at position: {elf}")
