from functools import lru_cache
import re
import parse_input

bag_dict = {}


def create_bag_dictionary(list_of_bag_attributes: list) -> dict:
    """Take in a list of bag attributes, for example:

    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.

    and create a dictionary to represent the relationship between bags.
    """
    for bag in list_of_bag_attributes:
        regex = re.compile(r'(\d)* *(\w+ \w+) bags*')
        bag_adjectives = re.findall(regex, bag)
        bag_key = bag_adjectives.pop(0)[1]
        bag_dict[bag_key] = bag_adjectives
    return bag_dict


catcher_array = []


@lru_cache()
def gold_bag_tardis(bag_key: str) -> int:
    """Figure out how many bags must be inside a shiny gold bag."""
    bag_count = 0
    if bag_key == "shiny gold":
        for bag_tuple in bag_dict[bag_key]:
            bag_count += int(bag_tuple[0])
    for bag_tuple in bag_dict[bag_key]:
        if bag_tuple[1] == "no other":
            bag_count = 1
        else:
            bag_count += (int(bag_tuple[0]) * gold_bag_tardis(bag_tuple[1]))
            print(f"{bag_tuple[0]} * {gold_bag_tardis(bag_tuple[1])}")
            catcher_array.append((int(bag_tuple[0]) * gold_bag_tardis(bag_tuple[1])))
    return bag_count


if __name__ == "__main__":
#    bag_guidelines = parse_input.input_per_line("../input")
#    bag_guidelines = ["shiny gold bags contain 2 dark red bags.",
#                   "dark red bags contain 2 dark orange bags.",
#                   "dark orange bags contain 2 dark yellow bags.",
#                   "dark yellow bags contain 2 dark green bags.",
#                   "dark green bags contain 2 dark blue bags.",
#                   "dark blue bags contain 2 dark violet bags.",
#                   "dark violet bags contain no other bags."]

#this passes answer is 6
#    bag_guidelines = ["shiny gold bags contain 2 dark red bags.",
#                      "dark red bags contain 2 dark orange bags.",
#                      "dark orange bags contain no other bags."]

    # should be 14 passes if you look at actual_bag Number
#    bag_guidelines = ["shiny gold bags contain 2 dark red bags.",
#                      "dark red bags contain 2 dark orange bags.",
#                      "dark orange bags contain 2 dark yellow bags.",
#                      "dark yellow bags contain no other bags."]

    bag_dict = create_bag_dictionary(bag_guidelines)
    bags_inside_gold = gold_bag_tardis("shiny gold")
    actual_bag_number = sum(catcher_array)
    print(f"{actual_bag_number} bags must be inside a shiny gold bag.")


# 142100 is too low
# 190655 is too high