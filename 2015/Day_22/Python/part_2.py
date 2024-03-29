from random import choice

# Spells
magic_missile = {"cost": 53, "damage": 4}
drain = {"cost": 73, "damage": 2, "heal": 2}
shield = {"cost": 113, "armor": 7, "effect_length": 6, "timer": 0}
poison = {"cost": 173, "damage": 3, "effect_length": 6, "timer": 0}
recharge = {"cost": 229, "mana_refill": 101, "effect_length": 5, "timer": 0}


def decide_spell():
    """Figure out which spell to cast."""
    spell_list = ["shield", "drain", "recharge", "poison", "magic_missile"]
    while True:
        cast_this_spell = choice(spell_list)
        if cast_this_spell == "shield":
            if shield["timer"] == 0 and wizard["mana_points"] >= shield["cost"]:
                print("chose shield")
                return "shield"
        elif cast_this_spell == "drain":
            if wizard["mana_points"] >= drain["cost"]:
                print("chose drain")
                return "drain"
        elif cast_this_spell == "recharge":
            if wizard["mana_points"] >= recharge["cost"] and recharge['timer'] == 0:
                print("chose recharge")
                return "recharge"
        elif cast_this_spell == "poison":
            if poison["timer"] == 0 and wizard["mana_points"] >= poison["cost"]:
                print("chose poison")
                return "poison"
        elif cast_this_spell == "magic_missile":
            if wizard["mana_points"] >= magic_missile["cost"]:
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
    if spell_name == "drain":
        wizard["mana_points"] -= drain["cost"]
        wizard["hit_points"] += drain["heal"]
        boss["hit_points"] -= drain["damage"]
        return drain["cost"]
    elif spell_name == "magic_missile":
        wizard["mana_points"] -= magic_missile["cost"]
        boss["hit_points"] -= magic_missile["damage"]
        return magic_missile["cost"]
    elif spell_name == "poison":
        wizard["mana_points"] -= poison["cost"]
        poison["timer"] = poison["effect_length"]
        return poison["cost"]
    elif spell_name == "recharge":
        wizard["mana_points"] -= recharge["cost"]
        recharge["timer"] = recharge["effect_length"]
        return recharge["cost"]
    elif spell_name == "shield":
        wizard["mana_points"] -= shield["cost"]
        wizard["armor"] += shield["armor"]
        shield["timer"] = shield["effect_length"]
        return shield["cost"]


def battle_sim():
    """Simulate a battle and return true if the player wins."""
    mana_spent = 0
    while True:
        print("--player turn--")
        print(f"Wizard: HP: {wizard['hit_points']}, Mana: {wizard['mana_points']}; Boss: {boss['hit_points']}")
        # hard mode - lost 1 HP before anything else happens
        wizard["hit_points"] -= 1
        if wizard["hit_points"] == 0:
            return False, mana_spent
        run_timer_spells()
        if wizard["mana_points"] <= 53 or wizard["hit_points"] <= 0:
            return False, mana_spent
        mana_spent += cast_spell(decide_spell())
        # boss turn
        print("--boss turn--")
        print(f"Wizard: HP: {wizard['hit_points']}, Mana: {wizard['mana_points']}; Boss: {boss['hit_points']}")
        run_timer_spells()
        print("Boss attacks 8")
        if boss["hit_points"] <= 0:
            # boss is dead
            return True, mana_spent
        wizard['hit_points'] = wizard['hit_points'] - (boss['damage'] - wizard['armor'])
        if wizard["hit_points"] <= 0:
            # wizard is dead
            return False, mana_spent


if __name__ == "__main__":
    mana_spent_to_win = 10000000000000000000
    for trial in range(100000):
        print(f"{trial=}")
        # set/reset wizard adn boss stats
        wizard = {"hit_points": 50, "mana_points": 500, "armor": 0}
        boss = {"hit_points": 55, "damage": 8}
        # set/reset spell timers
        shield["timer"] = 0
        poison["timer"] = 0
        recharge["timer"] = 0
        did_player_win, mana_spent_this_time = battle_sim()
        if did_player_win:
            print(f"Player won spent {mana_spent_this_time} mana")
            if mana_spent_this_time < mana_spent_to_win:
                mana_spent_to_win = mana_spent_this_time
        else:
            print(f"Player lost, spent {mana_spent_this_time} mana")
    print(f"To win required {mana_spent_to_win} mana.")
