from anytree import Node

def split_outer_inner_bags(bag_rule):
    return bag_rule.split('contain')


def split_inner_bags(inner_bags):
    return inner_bags.split(',')


def find_adjective_color(bag):
    bag_list = bag.split()
    return [[bag_list[position - 2], bag_list[position - 1]]
            for position, word in enumerate(bag_list)
            if word == "bag" or word == "bags"]


if __name__ == "__main__":
    with open('input', 'r') as file:
        bag_rules = file.readlines()
        for bag in bag_rules:
            outer_bag_name = find_adjective_color(split_outer_inner_bags(bag)[0])
            inner_bags_names = [find_adjective_color(inner_bag) for inner_bag in split_inner_bags(split_outer_inner_bags(bag)[1])]
