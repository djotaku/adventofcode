from . import part_1


def test_total_ingredients():
    butterscotch = ['-1', '-2', '6', '3', '8']
    cinnamon = ['2', '3', '-2', '-1', '3']
    cookie_score = part_1.ingredient_score([44, 56], [butterscotch, cinnamon])
    assert cookie_score == 62842880


def test_parse_ingredients():
    butterscotch = ['-1', '-2', '6', '3', '8']
    cinnamon = ['2', '3', '-2', '-1', '3']
    ingredient_inputs = ["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
                         "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"]
    assert part_1.parse_ingredients(ingredient_inputs) == [butterscotch, cinnamon]
