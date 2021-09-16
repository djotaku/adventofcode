from . import part_1_and_2


def test_battle_sim():
    player = {"hit_points": 8, "damage": 5, "armor": 5}
    boss = {"hit_points": 12, "damage": 7, "armor": 2}
    assert part_1_and_2.battle_sim(player, boss) is True
