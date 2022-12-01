"""Solution to Advent of Code 2022 Day 1: Counting Calories."""


def process_elves(calorie_file: str) -> list:
    """Go through our input to create a list of calorie sums."""
    elf_sum = 0
    calorie_list = []
    with open(calorie_file) as input_file:
        elf_calories = input_file.readlines()
        for this_line in elf_calories:
            if this_line != "\n":
                elf_sum += int(this_line)
            else:
                calorie_list.append(elf_sum)
                elf_sum = 0
    # account for the final elf
    calorie_list.append(elf_sum)
    return calorie_list


def find_top_3_calorie_sum(elf_cals: list) -> int:
    """Take in a list of elf calories, sort, and sum the top 3."""
    elf_cals.sort(reverse=True)
    return elf_cals[0] + elf_cals[1] + elf_cals[2]


if __name__ == "__main__":
    elf_calories = process_elves("../input.txt")
    max_calorie_elf = max(elf_calories)
    print(f"The elf with the most calories is carrying {max_calorie_elf} calories.")
    top_three_cals = find_top_3_calorie_sum(elf_calories)
    print(f"The top 3 elves are carrying {top_three_cals} calories.")
