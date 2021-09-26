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


@lru_cache()
def gold_bag_tardis(bag_key: str) -> int:
    """Figure out how many bags must be inside a shiny gold bag."""
    bag_count = 0
    for bag_tuple in bag_dict[bag_key]:
        if bag_tuple[1] == "no other":
            bag_count = 0
        else:
            print(f"There are {bag_tuple[0]} of {bag_tuple[1]} inside {bag_key}")
            bag_count += int(bag_tuple[0])
            inner_bag_count = gold_bag_tardis(bag_tuple[1])
            bag_count += int(bag_tuple[0]) * inner_bag_count
    return bag_count


if __name__ == "__main__":
    bag_guidelines = parse_input.input_per_line("../input")
    bag_dict = create_bag_dictionary(bag_guidelines)
    bags_inside_gold = gold_bag_tardis("shiny gold")
    print(f"{bags_inside_gold} bags must be inside a shiny gold bag.")


# 142100 is too low
# 190655 is too high