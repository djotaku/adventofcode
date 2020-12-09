class Bag:
    def __init__(self, name, parent, children):
        self.name = self.create_name(name)
        self.list_of_parent_bags = []
        self.list_of_child_bags = []
        self.inside_bags = 0
        if len(name) == 3:
            self.number_of_bags = name[0]
        else:
            self.number_of_bags = 0
        if parent is not None:
            self.add_parent_bag(parent)
        if children is not None:
            for child in children:
                self.add_child_bag(child)

    def create_name(self, name):
        if len(name) == 2:
            return f'{name[0]} {name[1]}'
        else:
            return f'{name[1]} {name[2]}'

    def add_parent_bag(self, parent):
        if parent not in self.list_of_parent_bags:
            self.list_of_parent_bags.append(parent)
            parent.add_child_bag(self)
            parent.inside_bags += self.number_of_bags

    def add_child_bag(self, child):
        if child not in self.list_of_child_bags:
            self.list_of_child_bags.append(child)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)


def split_outer_inner_bags(bag_rule):
    return bag_rule.split('contain')


def split_inner_bags(inner_bags):
    return inner_bags.split(',')


def find_adjective_color(bag):
    bag_list = bag.split()
    for position, word in enumerate(bag_list):
        if word == "bag" or word == "bags" or word == "bags." or word == "bag.":
            if len(bag_list) == 4:
                return [int(bag_list[position - 3]), bag_list[position - 2], bag_list[position - 1]]
            else:
                return [bag_list[position - 2], bag_list[position - 1]]


def recursive_count(list_of_bags):
    ancestors = []
    inner_bags = 1
    for bag in list_of_bags:
        if len(bag.list_of_child_bags) == 0:
            if bag.name != "no other":
                inner_bags = inner_bags * bag.number_of_bags
            ancestors.append(bag)
        else:
            inner_bags = inner_bags * bag.number_of_bags
            ancestors.append(bag)
            ancestors += recursive_count(bag.list_of_child_bags)
    return ancestors


if __name__ == "__main__":
    with open('input', 'r') as file:
        bag_rules = file.readlines()
        all_bags = []
        for bag in bag_rules:
            outer_bag_name = find_adjective_color(split_outer_inner_bags(bag)[0])
            inner_bags_names = [find_adjective_color(inner_bag)
                                for inner_bag in split_inner_bags(split_outer_inner_bags(bag)[1])]
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
            else:
                for already_extant_outer_bag in all_bags:
                    if already_extant_outer_bag == outer_bag:
                        for a_bag in inner_bags_names:
                            inner_bag = Bag(a_bag, already_extant_outer_bag, None)
                            if inner_bag not in all_bags:
                                all_bags.append(inner_bag)
                            else:
                                for already_bag in all_bags:
                                    if already_bag == inner_bag:
                                        already_bag.add_parent_bag(already_extant_outer_bag)
        # for debugging
        for bag in all_bags:
            if bag.name == "shiny gold":
                print(f'{bag.name=}')
                for child in bag.list_of_child_bags:
                    print(f'{child.name=}')
                    for grandchild in child.list_of_child_bags:
                        print(f'{grandchild.name=}')
                print('----------------\n')
        # end debugging
        for bag in all_bags:
            if bag.name == "shiny gold":
                print(bag.inside_bags)
                descendant_count = recursive_count(bag.list_of_child_bags)

        baggies = 1
        for bag in descendant_count:
            print(f'{bag.name}')
            print(f'{bag.number_of_bags=}')
            print(f'{bag.inside_bags=}')
            if bag.name != "no other":
                if bag.number_of_bags != 0:
                    baggies *= bag.number_of_bags
        print(baggies)

