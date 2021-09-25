import re
import parse_input


def create_bag_dictionary(list_of_bag_attributes: list) -> dict:
    """Take in a list of bag attributes, for example:

    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.

    and create a dictionary to represent the relationship between bags.
    """
    bag_dict = {}
    for bag in list_of_bag_attributes:
        regex = re.compile(r'(\d)* *(\w+ \w+) bags*')
        bag_adjectives = re.findall(regex, bag)
        bag_key = bag_adjectives.pop(0)[1]
        print(bag_key)
        bag_dict[bag_key] = bag_adjectives
    return bag_dict


def find_gold_bags(bag_dictionary: dict) -> int:
    """Take a dictionary of bag rules and figure out if it can eventually hold a gold bag.
    Return how many can eventually contain a gold bag.
    """
    bag_count = 0
    for key in bag_dictionary.keys():
        if bag_dictionary[key].contains("shiny gold"):
            bag_count += 1
        else:
            pass