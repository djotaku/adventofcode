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

def parse_ingredients(ingredient_input)
  ingredient_input.map{|x| x.scan(/-*\d/)}
end

def brute_force_cooke_score(ingredient_list)
  (1..100).to_a.permutation(ingredient_list.size).lazy.map { |p| p.sum == 100 ? 0 : ingredient_score(p, ingredient_list) }.max
end

if $PROGRAM_NAME == __FILE__
  cookie_list = input_per_line('../input.txt')
  ingredients = parse_ingredients(cookie_list)
  cookie_score = brute_force_cooke_score(ingredients)
  puts "The cookie score is #{cookie_score}"
end