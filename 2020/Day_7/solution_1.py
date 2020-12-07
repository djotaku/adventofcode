class Bag:
    def __init__(self, name, parent, **kwargs):
        self.name = self.name(name)
        self.list_of_parent_bags = []
        self.add_parent_bag(parent)
        self.list_of_child_bags = []
        for child in kwargs.values():
            self.add_child_bag(child)

    def name(self, name):
        return f'{name[0][0]} {name[0][1]}'

    def add_parent_bag(self, parent):
        if parent is None:
            return
        if f'{parent[0][0]} {parent[0][1]}' not in self.list_of_parent_bags:
            self.list_of_parent_bags.append(f'{parent[0][0]} {parent[0][1]}')

    def add_child_bag(self, child):
        if child is None:
            pass
        if f'{child[0][0]} {child[0][1]}' not in self.list_of_parent_bags:
            self.list_of_child_bags.append(f'{child[0][0]} {child[0][1]}')


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
        all_bags = []
        for bag in bag_rules:
            outer_bag = find_adjective_color(split_outer_inner_bags(bag)[0])
            inner_bags = [find_adjective_color(inner_bag) for inner_bag in split_inner_bags(split_outer_inner_bags(bag)[1])]
