WEAPONS = {"Dagger"=> {"cost"=> 8, "damage"=> 4, "armor"=> 0},
           "Shortsword"=> {"cost"=> 10, "damage"=> 5, "armor"=> 0},
           "Warhammer"=> {"cost"=> 25, "damage"=> 6, "armor"=> 0},
           "Longsword"=> {"cost"=> 40, "damage"=> 7, "armor"=> 0},
           "Greataxe"=> {"cost"=> 74, "damage"=> 8, "armor"=> 0}}

ARMOR = {"Leather"=> {"cost"=> 13, "damage"=> 0, "armor"=> 1},
         "Chainmail"=> {"cost"=> 31, "damage"=> 0, "armor"=> 2},
         "Splintmail"=> {"cost"=> 53, "damage"=> 0, "armor"=> 3},
         "Bandedmail"=> {"cost"=> 75, "damage"=> 0, "armor"=> 4},
         "Platemail"=> {"cost"=> 102, "damage"=> 0, "armor"=> 5},
         "NoMail"=> {"cost"=> 0, "damage"=> 0, "armor"=> 0}}

RINGS = {"Damage +1"=> {"cost"=> 25, "damage"=> 1, "armor"=> 0},
         "Damage +2"=> {"cost"=> 50, "damage"=> 2, "armor"=> 0},
         "Damage +3"=> {"cost"=> 100, "damage"=> 3, "armor"=> 0},
         "Defense +1"=> {"cost"=> 20, "damage"=> 0, "armor"=> 1},
         "Defense +2"=> {"cost"=> 40, "damage"=> 0, "armor"=> 2},
         "Defense +3"=> {"cost"=> 80, "damage"=> 0, "armor"=> 3},
         "NoRing"=> {"cost"=> 0, "damage"=> 0, "armor"=> 0}}

weapons = WEAPONS.keys
armor = ARMOR.keys
left_hand = RINGS.keys
right_hand = RINGS.keys

all_battle_combinations = weapons.product(armor, left_hand, right_hand)

def battle_sim(player, enemy)
  while true
    enemy["hit_points"] = enemy["hit_points"] - (player['damage'] - enemy["armor"])
    if enemy["hit_points"] <= 0
      return true
    end
    player['hit_points'] = player['hit_points'] - (enemy['damage'] - player['armor'])
        if player["hit_points"] <= 0
          return false
        end
  end
end

def equip_player(equipment)
  {'hit_points'=> 100,
   'damage'=> WEAPONS[equipment[0]]["damage"] + ARMOR[equipment[1]]["damage"] + RINGS[equipment[2]]["damage"] + RINGS[equipment[3]]["damage"],
   'armor'=> WEAPONS[equipment[0]]['armor'] + ARMOR[equipment[1]]["armor"] + RINGS[equipment[2]]['armor'] + RINGS[equipment[3]]['armor'],
   'cost'=> WEAPONS[equipment[0]]['cost'] + ARMOR[equipment[1]]['cost'] + RINGS[equipment[2]]['cost'] + RINGS[equipment[3]]['cost'],
    }
end

BOSS = {'hit_points'=> 100, 'damage'=> 8, 'armor'=> 2}

cost_to_win = 1000000000000000
cost_to_lose = 0
all_battle_combinations.each do |combination|
  player = equip_player(combination)
  BOSS['hit_points'] = 100
  if battle_sim(player, BOSS)
    cost_to_win = [player['cost'], cost_to_win].min
  else
    cost_to_lose = [player['cost'], cost_to_lose].max
  end
end
puts "-----------------------------------------------------------------"
puts"-------------------- Part 1 -------------------------------------"
puts"The least gold that can be spent to win is #{cost_to_win}."
puts"-----------------------------------------------------------------"
puts"-------------------- Part 2 -------------------------------------"
puts"The most gold that can be spent and still lose is #{cost_to_lose}."
puts"-----------------------------------------------------------------"