from sys import path
import re
path.insert(0, '../../input_parsing')
import parse_input


def ingredient_score(teaspoon_list, ingredient_list):
    combined_list = zip(teaspoon_list, ingredient_list)
    total_ingredients = []
    for multiplication_tuple in combined_list:
        temp_list = [
            int(item) * multiplication_tuple[0] for item in multiplication_tuple[1]
        ]
        total_ingredients.append(temp_list)
    properties = zip(*total_ingredients)
    final_score = 1
    property_count = 1  # this is to ignore calories for part 1
    for cookie_property in properties:
        final_score *= sum(cookie_property)
        property_count += 1
        if property_count == 5:
            break
    return final_score


def parse_ingredients(ingredient_inputs):
    pattern = re.compile(r'(-*\d)')
    return [re.findall(pattern, ingredient) for ingredient in ingredient_inputs]
