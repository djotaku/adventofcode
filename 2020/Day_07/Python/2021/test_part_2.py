import part_2


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
    bag_dict = part_2.create_bag_dictionary(bag_rules)
    assert bag_dict["light red"] == [("1", "bright white"), ("2", "muted yellow")]
    assert bag_dict["bright white"] == [('1', 'shiny gold')]
    assert bag_dict["dotted black"] == [('', "no other")]


def test_gold_bag_tardis():
    bags_inside = part_2.gold_bag_tardis("shiny gold")
    assert bags_inside == 32


#def test_gold_bag_tardis_2():
#    bag_rules_2 = ["shiny gold bags contain 2 dark red bags.",
#                   "dark red bags contain 2 dark orange bags.",
#                   "dark orange bags contain 2 dark yellow bags.",
#                   "dark yellow bags contain 2 dark green bags.",
#                   "dark green bags contain 2 dark blue bags.",
#                   "dark blue bags contain 2 dark violet bags.",
#                   "dark violet bags contain no other bags."]
#    part_2.bag_dict = part_2.create_bag_dictionary(bag_rules_2)
#    print(part_2.bag_dict)
#    bags_inside_2 = part_2.gold_bag_tardis("shiny gold")
#    assert bags_inside_2 == 126
