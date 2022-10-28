"""Solution for AoC Day 19: An Elephant Named Joseph"""


def game_round(elfs_and_presents: dict) -> dict:
    """play one round of the white elephant game."""
    elves_still_in_game = list(elfs_and_presents.keys())
    for playing_elf, present_status in elf_presents.items():
        if present_status:
            if playing_elf == len(elf_presents.keys()):
                elf_presents[elves_still_in_game[0]] = False
            else:
                elf_presents[elf + 1] = False
    elves_to_delete = []
    for key, item in elfs_and_presents:
        if item is False:
            elves_to_delete.append(elfs_and_presents[key])
    for the_elf in elves_to_delete:
        del(elfs_and_presents[the_elf])
    return elfs_and_presents


if __name__ == "__main__":
    ELVES = 5
    elf_presents = {}
    for elf in range(1, ELVES + 1):
        elf_presents[elf] = True
    while len(elf_presents) > 1:
        elf_presents = game_round(elf_presents)
    print(elf_presents.keys())
