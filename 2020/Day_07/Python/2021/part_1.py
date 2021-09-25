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
def find_gold_bag_carriers(bag_key: str) -> int:
    """Take a dictionary of bag rules and figure out if it can eventually hold a gold bag.
    Return how many can eventually contain a gold bag.
    """
    shiny_count = 0
    for bag_tuple in bag_dict[bag_key]:
        if bag_tuple[1] == "shiny gold":
            shiny_count = 1
        elif bag_tuple[1] == "no other":
            shiny_count += 0
        else:
            shiny_count += find_gold_bag_carriers(bag_tuple[1])
            if shiny_count > 0:
                break
    return shiny_count


if __name__ == "__main__":
    bag_guidelines = parse_input.input_per_line("../input")
    bag_dict = create_bag_dictionary(bag_guidelines)
    gold_bag_carrier_count = sum(find_gold_bag_carriers(bag) for bag in bag_dict.keys())
    print(f"{gold_bag_carrier_count} bags eventually can contain at least one shiny gold bag")
