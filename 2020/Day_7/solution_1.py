class Bag:
    def __init__(self, name, parent, children):
        self.name = self.name(name)
        self.list_of_parent_bags = []
        if parent is not None:
            self.add_parent_bag(parent)
        self.list_of_child_bags = []
        if children is not None:
            for child in children:
                self.add_child_bag(child)

    def name(self, name):
        if name != []:
            return f'{name[0][0]} {name[0][1]}'

    def add_parent_bag(self, parent):
        if parent not in self.list_of_parent_bags:
            self.list_of_parent_bags.append(parent)
            parent.add_child_bag(self)

    def add_child_bag(self, child):
        if child not in self.list_of_parent_bags:
            self.list_of_child_bags.append(child)

    def __eq__(self, other):
        return self.name == other.name


def split_outer_inner_bags(bag_rule):
    return bag_rule.split('contain')


def split_inner_bags(inner_bags):
    return inner_bags.split(',')


def find_adjective_color(bag):
    bag_list = bag.split()
    return [[bag_list[position - 2], bag_list[position - 1]]
            for position, word in enumerate(bag_list)
            if word == "bag" or word == "bags"]


def recursive_count(list_of_bags):
    print(len(list_of_bags))
    for bag in list_of_bags:
        if len(bag.list_of_parent_bags) == 0:
            return 1
        else:
            return recursive_count(bag.list_of_parent_bags)


if __name__ == "__main__":
    with open('input', 'r') as file:
        bag_rules = file.readlines()
        all_bags = []
        for bag in bag_rules:
            outer_bag_name = find_adjective_color(split_outer_inner_bags(bag)[0])
            inner_bags_names = [find_adjective_color(inner_bag) for inner_bag in split_inner_bags(split_outer_inner_bags(bag)[1])]
            inner_bags_names.remove([])
            outer_bag = Bag(outer_bag_name, None, None)
            if outer_bag not in all_bags:
                all_bags.append(outer_bag)
            for a_bag in inner_bags_names:
                inner_bag = Bag(a_bag, outer_bag, None)
                if inner_bag not in all_bags:
                    all_bags.append(inner_bag)
                else:
                    for already_bag in all_bags:
                        if already_bag == inner_bag:
                            already_bag.add_parent_bag(outer_bag)
        master_bags = 0
        for bag in all_bags:
            if bag.name == "shiny gold":
                master_bags = master_bags + len(bag.list_of_parent_bags)
                master_bags = master_bags + recursive_count(bag.list_of_parent_bags)

        print(f'{master_bags=}')

# 15 is not answer
# 11 is not answer