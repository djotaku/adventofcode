from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def ingredient_score(teaspoon_list, ingredient_list):
    combined_list = zip(teaspoon_list, ingredient_list)
    total_ingredients = []
    for multiplication_tuple in combined_list:
        temp_list = [
            item * multiplication_tuple[0] for item in multiplication_tuple[1]
        ]
        total_ingredients.append(temp_list)
    properties = zip(*total_ingredients)
    final_score = 1
    for cookie_property in properties:
        final_score *= sum(cookie_property)
    return final_score
