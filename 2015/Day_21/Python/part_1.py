from sys import path
path.insert(0, '../../input_parsing')
import parse_input


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
        print(f"Player: {player['hit_points']}; Enemy: {enemy['hit_points']}")
    return player['hit_points'] > 0

