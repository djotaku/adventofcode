from . import part_2


def test_total_ingredients():
    butterscotch = ['-1', '-2', '6', '3', '8']
    cinnamon = ['2', '3', '-2', '-1', '3']
    cookie_score = part_2.ingredient_score([44, 56], [butterscotch, cinnamon])
    assert cookie_score == 62842880


def test_parse_ingredients():
    butterscotch = ['-1', '-2', '6', '3', '8']
    cinnamon = ['2', '3', '-2', '-1', '3']
    ingredient_inputs = ["Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
                         "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"]
    assert part_2.parse_ingredients(ingredient_inputs) == [butterscotch, cinnamon]


def test_brute_force_cookie_score():
    butterscotch = ['-1', '-2', '6', '3', '8']
    cinnamon = ['2', '3', '-2', '-1', '3']
    assert part_2.brute_force_cookie_score([butterscotch, cinnamon]) == 57600000


def test_count_calories():
    butterscotch = ['-1', '-2', '6', '3', '8']
    cinnamon = ['2', '3', '-2', '-1', '3']
    assert part_2.count_calories([40, 60], [butterscotch, cinnamon]) == 500
