import part_1

bag_rules = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
             "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
             "bright white bags contain 1 shiny gold bag.",
             "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
             "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
             "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
             "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
             "faded blue bags contain no other bags.",
             "dotted black bags contain no other bags."]


def test_create_bag_dictionary():
    bag_dict = part_1.create_bag_dictionary(bag_rules)
    assert bag_dict["light red"] == [("1", "bright white"), ("2", "muted yellow")]
    assert bag_dict["bright white"] == [('1', 'shiny gold')]
    assert bag_dict["dotted black"] == [('', "no other")]


def test_find_gold_bag_carriers():
    bag_dict = part_1.create_bag_dictionary(bag_rules)
    gold_bag_carrier_count = sum(part_1.find_gold_bag_carriers(bag) for bag in bag_dict.keys())
    assert gold_bag_carrier_count == 4
