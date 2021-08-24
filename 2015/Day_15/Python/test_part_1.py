from . import part_1


def test_total_ingredients():
    butterscotch = [-1, -2, 6, 3]
    cinnamon = [2, 3, -2, -1]
    cookie_score = part_1.ingredient_score([44, 56], [butterscotch, cinnamon])
    assert cookie_score == 62842880
