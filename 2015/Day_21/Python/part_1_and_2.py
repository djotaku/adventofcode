from itertools import product

WEAPONS = {"Dagger": {"cost": 8, "damage": 4, "armor": 0},
           "Shortsword": {"cost": 10, "damage": 5, "armor": 0},
           "Warhammer": {"cost": 25, "damage": 6, "armor": 0},
           "Longsword": {"cost": 40, "damage": 7, "armor": 0},
           "Greataxe": {"cost": 74, "damage": 8, "armor": 0}}

ARMOR = {"Leather": {"cost": 13, "damage": 0, "armor": 1},
         "Chainmail": {"cost": 31, "damage": 0, "armor": 2},
         "Splintmail": {"cost": 53, "damage": 0, "armor": 3},
         "Bandedmail": {"cost": 75, "damage": 0, "armor": 4},
         "Platemail": {"cost": 102, "damage": 0, "armor": 5},
         "NoMail": {"cost": 0, "damage": 0, "armor": 0}}

RINGS = {"Damage +1": {"cost": 25, "damage": 1, "armor": 0},
         "Damage +2": {"cost": 50, "damage": 2, "armor": 0},
         "Damage +3": {"cost": 100, "damage": 3, "armor": 0},
         "Defense +1": {"cost": 20, "damage": 0, "armor": 1},
         "Defense +2": {"cost": 40, "damage": 0, "armor": 2},
         "Defense +3": {"cost": 80, "damage": 0, "armor": 3},
         "NoRing": {"cost": 0, "damage": 0, "armor": 0}}

weapons = [key for key in WEAPONS.keys()]
armor = [key for key in ARMOR.keys()]
left_hand = [key for key in RINGS.keys()]
right_hand = [key for key in RINGS.keys()]

all_battle_combinations = product(weapons, armor, left_hand, right_hand)


def battle_sim(player: dict, enemy: dict) -> bool:
    """Simulate a battle and return true if the player wins."""
    while True:
        enemy["hit_points"] = enemy["hit_points"] - (player['damage'] - enemy["armor"])
        if enemy["hit_points"] <= 0:
            break
        player['hit_points'] = player['hit_points'] - (enemy['damage'] - player['armor'])
        if player["hit_points"] <= 0:
            break
        # debug
        # print(f"Player: {player['hit_points']}; Enemy: {enemy['hit_points']}")
    return player['hit_points'] > 0


def equip_player(equipment: tuple) -> dict:
    """Determine the equipment the player is wearing and the cost. Output is a player dict."""
    return {
        'hit_points': 100,
        'damage': (
            WEAPONS[equipment[0]]['damage']
            + ARMOR[equipment[1]]['damage']
            + RINGS[equipment[2]]['damage']
            + RINGS[equipment[3]]['damage']
        ),
        'armor': (
            WEAPONS[equipment[0]]['armor']
            + ARMOR[equipment[1]]['armor']
            + RINGS[equipment[2]]['armor']
            + RINGS[equipment[3]]['armor']
        ),
        'cost': (
            WEAPONS[equipment[0]]['cost']
            + ARMOR[equipment[1]]['cost']
            + RINGS[equipment[2]]['cost']
            + RINGS[equipment[3]]['cost']
        ),
    }


BOSS = {'hit_points': 100, 'damage': 8, 'armor': 2}

if __name__ == "__main__":
    cost_to_win = 1000000000000000
    for combination in all_battle_combinations:
        player = equip_player(combination)
        BOSS['hit_points'] = 100
        # debug
        # print(player)
        if battle_sim(player, BOSS):
            if player['cost'] < cost_to_win:
                cost_to_win = player['cost']
    print("----------------------------------------------------------")
    print("-------------------- Part 1 ------------------------------")
    print(f"The least gold that can be spent to win is {cost_to_win}.")
    print("----------------------------------------------------------")
    cost_to_lose = 0
    for combination in all_battle_combinations:
        player = equip_player(combination)
        print(player)
        BOSS['hit_points'] = 100
        if not battle_sim(player, BOSS):
            if player['cost'] > cost_to_lose:
                cost_to_lose = player['cost']
    print("-------------------- Part 2 -------------------------------------")
    print(f"The most gold that can be spent and still lose is {cost_to_lose}.")
