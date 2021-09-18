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
        shield["timer"] -= 1
    if poison["timer"] > 0:
        boss["hit_points"] -= poison["damage"]
        poison["timer"] -= 1
    if recharge["timer"] > 0:
        wizard["mana_points"] += recharge["mana_refill"]
        recharge["timer"] -= 1


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
    mana_spent = 0
    while True:
        # player turn
        run_timer_spells()
        mana_spent += cast_spell(decide_spell())
        if wizard["mana_points"] <= 0:
            break
        # boss turn
        run_timer_spells()
        wizard['hit_points'] = wizard['hit_points'] - (boss['damage'] - wizard['armor'])
        if boss["hit_points"] <= 0:
            break
        if wizard["hit_points"] <= 0:
            break
        # debug
        print(f"Wizard: HP: {wizard['hit_points']}, Mana: {wizard['mana_points']}; Boss: {boss['hit_points']}")
    # return wizard['hit_points'] > 0 and wizard["mana_points"] > 0
    print("battle sim ended. Final tallies:\n")
    print(f"Wizard: HP: {wizard['hit_points']}, Mana: {wizard['mana_points']}; Boss: {boss['hit_points']}")
    return mana_spent


if __name__ == "__main__":
    mana_spent = battle_sim()
    print(f"To win required {mana_spent} mana.")


# 551 is too low