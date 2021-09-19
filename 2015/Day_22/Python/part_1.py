from random import choice

# Spells
magic_missile = {"cost": 53, "damage": 4}
drain = {"cost": 73, "damage": 2, "heal": 2}
shield = {"cost": 113, "armor": 7, "effect_length": 6, "timer": 0}
poison = {"cost": 173, "damage": 3, "effect_length": 6, "timer": 0}
recharge = {"cost": 229, "mana_refill": 101, "effect_length": 5, "timer": 0}

wizard = {"hit_points": 50, "mana_points": 500, "armor": 0}
boss = {"hit_points": 55, "damage": 8}


def decide_spell():
    """Figure out which spell to cast."""
    if wizard["hit_points"] == 2 and shield["timer"] == 0 and wizard["mana_points"] >= shield["cost"]:
        # debug
        print("chose shield")
        return "shield"
    elif wizard["hit_points"] == 1 and wizard["mana_points"] >= drain["cost"]:
        # debug
        print("chose drain")
        return "drain"
    elif (229+53) >= wizard["mana_points"] >= 229 and recharge['timer'] == 0:
        # debug
        print("chose recharge")
        return "recharge"
    elif poison["timer"] == 0 and wizard["mana_points"] >= poison["cost"]:
        # debug
        print("chose poison")
        return "poison"
    else:
        print("chose magic missile")
        return "magic_missile"


def run_timer_spells():
    if shield["timer"] > 0:
        print("Shield active")
        shield["timer"] -= 1
        print(f'Shield timer drops to {shield["timer"]}')
        if shield["timer"] == 0:
            print("Shield has expired, lowering wizard armor")
            wizard["armor"] -= shield["armor"]
    if poison["timer"] > 0:
        print("Poison active")
        boss["hit_points"] -= poison["damage"]
        print(f"Poison attacks boss for {poison['damage']}")
        poison["timer"] -= 1
        print(f'Poison timer drops to {poison["timer"]}')
    if recharge["timer"] > 0:
        print("Recharge active")
        wizard["mana_points"] += recharge["mana_refill"]
        print(f"Mana refilled by +{recharge['mana_refill']}")
        recharge["timer"] -= 1
        print(f"Recharge drops to {recharge['timer']}")


def cast_spell(spell_name: str):
    if spell_name == "magic_missile":
        wizard["mana_points"] -= magic_missile["cost"]
        boss["hit_points"] -= magic_missile["damage"]
        return magic_missile["cost"]
    elif spell_name == "drain":
        wizard["mana_points"] -= drain["cost"]
        wizard["hit_points"] += drain["heal"]
        boss["hit_points"] -= drain["damage"]
        return drain["cost"]
    elif spell_name == "shield":
        wizard["mana_points"] -= shield["cost"]
        wizard["armor"] += shield["armor"]
        shield["timer"] = shield["effect_length"]
        return shield["cost"]
    elif spell_name == "poison":
        wizard["mana_points"] -= poison["cost"]
        poison["timer"] = poison["effect_length"]
        return poison["cost"]
    elif spell_name == "recharge":
        wizard["mana_points"] -= recharge["cost"]
        recharge["timer"] = recharge["effect_length"]
        return recharge["cost"]


def battle_sim():
    """Simulate a battle and return true if the player wins."""
    player_wins = False
    mana_spent = 0
    spell_list = ["shield", "drain", "recharge", "poison", "magic_missile"]
    while True:
        print("--player turn--")
        run_timer_spells()
        # mana_spent += cast_spell(decide_spell())
        mana_spent += cast_spell(choice(spell_list))
        if wizard["mana_points"] <= 0:
            return player_wins, mana_spent
        print(f"Wizard: HP: {wizard['hit_points']}, Mana: {wizard['mana_points']}; Boss: {boss['hit_points']}")
        # boss turn
        print("--boss turn--")
        run_timer_spells()
        wizard['hit_points'] = wizard['hit_points'] - (boss['damage'] - wizard['armor'])
        if boss["hit_points"] <= 0:
            player_wins = True
            return player_wins, mana_spent
        if wizard["hit_points"] <= 0:
            return player_wins, mana_spent
        # debug
        print(f"Wizard: HP: {wizard['hit_points']}, Mana: {wizard['mana_points']}; Boss: {boss['hit_points']}")
    # return wizard['hit_points'] > 0 and wizard["mana_points"] > 0
    print("battle sim ended. Final tallies:\n")
    print(f"Wizard: HP: {wizard['hit_points']}, Mana: {wizard['mana_points']}; Boss: {boss['hit_points']}")
    return player_wins, mana_spent


if __name__ == "__main__":
    mana_spent = 10000000000000000000
    player_wins = False
    for trial in range(1000000):
        wizard = {"hit_points": 50, "mana_points": 500, "armor": 0}
        boss = {"hit_points": 55, "damage": 8}
        player_wins, mana_spent_this_time = battle_sim()
        if player_wins:
            if mana_spent_this_time < mana_spent:
                mana_spent = mana_spent_this_time
    print(f"To win required {mana_spent} mana.")


# 551 is too low
# 4741 is too high
# 2414 is too high