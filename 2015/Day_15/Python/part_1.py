from sys import path
from itertools import permutations, combinations_with_replacement
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
        if sum(cookie_property) > 0:
            final_score *= sum(cookie_property)
        property_count += 1
        if property_count == 5:
            break
    return final_score


def parse_ingredients(ingredient_inputs):
    pattern = re.compile(r'(-*\d)')
    return [re.findall(pattern, ingredient) for ingredient in ingredient_inputs]


#def maximize_cookie_score(ingredient_list):
#    starting_point = 110 / len(ingredient_list)
#    score = 0
#    original_teaspoons = [starting_point for ingredient in ingredient_list]
#    teaspoons = original_teaspoons.copy()
#    amount_to_increase = len(ingredient_list) - 1
#    for x in range(0, len(teaspoons)-1):
#        while teaspoons[x] <= 100:
#            teaspoons[x] += amount_to_increase
#            for y in range()


def brute_force_cookie_score(ingredient_list):
    ingredient_combos = [
        element
        for element in permutations(
            range(1, 100), len(ingredient_list)
        )
        if sum(element) == 100
    ]
    score = 0
    for ingredient_combination in ingredient_combos:
        combo_score = ingredient_score(ingredient_combination, ingredient_list)
        if combo_score > score:
            score = combo_score
    return score


if __name__ == "__main__":
    cookie_list = parse_input.input_per_line('../input.txt')
    ingredients = parse_ingredients(cookie_list)
    cookie_score = brute_force_cookie_score(ingredients)
    print(f"The cookie score is {cookie_score}")


# 19150560 is too low
