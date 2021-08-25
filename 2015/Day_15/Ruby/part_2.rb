require "../../input_parsing/parse_input"

def ingredient_score(multipliers, cookies)
  intermediate = multipliers.zip(cookies)
  product = []
  intermediate.each do |multiplication_item|
  temp_list = multiplication_item[1].map{|x| multiplication_item[0] * x.to_i}
  product.append(temp_list)
  temp_list = []
  end
  properties = product.transpose
  final_score = 1
  property_count = 1
  properties.each do |cookie_property|
    if cookie_property.sum > 0
      final_score *= cookie_property.sum
    end
  property_count += 1
  if property_count == 5
    break
  end
  end
  final_score
end

def count_calories(teaspoon_list, ingredient_list)
  (0..ingredient_list.length).map{|index| teaspoon_list[index] * ingredient_list[index][-1].to_i}.sum
end

def parse_ingredients(ingredient_input)
  ingredient_input.map{|x| x.scan(/-*\d/)}
end

def brute_force_cooke_score(ingredient_list)
  combos = (1..100).to_a
          .permutation(ingredient_list.length)
          .select{|x|x if x.sum == 100 }
  score = 0
  combos.each do |ingredient_combo|
    combo_score = ingredient_score(ingredient_combo, ingredient_list)
    calorie_score = count_calories(ingredient_combo, ingredient_list)
    if combo_score > score and calorie_score == 500
      score = combo_score
    end
  end
  score
end

if $PROGRAM_NAME == __FILE__
  cookie_list = input_per_line('../input.txt')
  ingredients = parse_ingredients(cookie_list)
  cookie_score = brute_force_cooke_score(ingredients)
  puts "The cookie score is #{cookie_score}"
end