# Spells
MAGIC_MISSILE = {"cost"=> 53, "damage"=> 4}
DRAIN = {"cost"=> 73, "damage"=> 2, "heal"=> 2}
SHIELD = {"cost"=> 113, "armor"=> 7, "effect_length"=> 6, "timer"=> 0}
POISON = {"cost"=> 173, "damage"=> 3, "effect_length"=> 6, "timer"=> 0}
RECHARGE = {"cost"=> 229, "mana_refill"=> 101, "effect_length"=> 5, "timer"=> 0}

def decide_spell
  spell_list = %w[shield drain recharge poison magic_missile]
  while true
    cast_this_spell = spell_list.sample
    case cast_this_spell
    when "shield"
      if SHIELD["timer"] == 0 and WIZARD["mana_points"] >= SHIELD["cost"]
        return "shield"
      end
    when "drain"
        if WIZARD["mana_points"] >= DRAIN["cost"]
          return "drain"
        end
    when "recharge"
      if WIZARD["mana_points"] >= RECHARGE["cost"] and RECHARGE['timer'] == 0
        return "recharge"
      end
    when "poison"
      if POISON["timer"] == 0 and WIZARD["mana_points"] >= POISON["cost"]
        return "poison"
      end
    when "magic_missile"
      if WIZARD["mana_points"] >= MAGIC_MISSILE["cost"]
        return "magic_missile"
      end
    else
      puts "You should never get here."
    end
  end
end

def run_timer_spells
  #puts "running timer spells"
  if SHIELD["timer"] > 0
    SHIELD["timer"] -= 1
    WIZARD["armor"] -= SHIELD["armor"] if SHIELD["timer"] == 0
  end
  if POISON["timer"] > 0
    BOSS["hit_points"] -= POISON["damage"]
    POISON["timer"] -= 1
  end
  if RECHARGE["timer"] > 0
    WIZARD["mana_points"] += RECHARGE["mana_refill"]
    RECHARGE["timer"] -= 1
  end
end

def cast_spell(spell_name)
  case spell_name
  when "drain"
    WIZARD["mana_points"] -= DRAIN["cost"]
    WIZARD["hit_points"] += DRAIN["heal"]
    BOSS["hit_points"] -= DRAIN["damage"]
    return DRAIN["cost"]
  when "magic_missile"
    WIZARD["mana_points"] -= MAGIC_MISSILE["cost"]
    BOSS["hit_points"] -= MAGIC_MISSILE["damage"]
    return MAGIC_MISSILE["cost"]
  when "poison"
    WIZARD["mana_points"] -= POISON["cost"]
    POISON["timer"] = POISON["effect_length"]
    return POISON["cost"]
  when "recharge"
    WIZARD["mana_points"] -= RECHARGE["cost"]
    RECHARGE["timer"] = RECHARGE["effect_length"]
    return RECHARGE["cost"]
  when "shield"
    WIZARD["mana_points"] -= SHIELD["cost"]
    WIZARD["armor"] += SHIELD["armor"]
    SHIELD["timer"] = SHIELD["effect_length"]
    return SHIELD["cost"]
  else
    puts "You should never get here."
  end
end

def battle_sim
  mana_spent = 0
  while true
    # wizard turn
    #puts "wizard turn"
    # puts WIZARD
    WIZARD["hit_points"] -= 1
    return [false, mana_spent] if WIZARD["hit_points"] <= 0
    run_timer_spells
    return [false, mana_spent] if WIZARD["mana_points"] <= 53 or WIZARD["hit_points"] <= 0
    mana_spent += cast_spell(decide_spell)
    # puts mana_spent
    # boss turn
    #puts "boss turn"
    run_timer_spells
    return [true, mana_spent] if BOSS["hit_points"] <= 0
    WIZARD['hit_points'] = WIZARD['hit_points'] - (BOSS['damage'] - WIZARD['armor'])
    return [false, mana_spent] if WIZARD["hit_points"] <= 0
  end
end

mana_spent_to_win = 10000000000000000000
(1..100000).each do |trial|
  # puts trial
  WIZARD = {"hit_points"=> 50, "mana_points"=> 500, "armor"=> 0}
  BOSS = {"hit_points"=> 55, "damage"=> 8}
  SHIELD["timer"] = 0
  POISON["timer"] = 0
  RECHARGE["timer"] = 0
  did_player_win, mana_spent_this_time = battle_sim
  if did_player_win
    puts "player wins with #{mana_spent_this_time}"
    mana_spent_to_win = [mana_spent_to_win, mana_spent_this_time].min
  else
    puts "Player lost with #{mana_spent_this_time}"
  end
end
puts "Player spent #{mana_spent_to_win} mana to win."