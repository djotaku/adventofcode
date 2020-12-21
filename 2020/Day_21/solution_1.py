from collections import Counter

def grab_input(input_file):
    with open(input_file, 'r') as file:
        return [line.rstrip('\n') for line in file.readlines()]


def create_clean_dictionary_names(line):
    if ',' in line:
        step_1 = line.split(', ')
        list_to_return = [step_1[0].lstrip('contains ')]
        for allergen in step_1[1:]:
            list_to_return.append(allergen.rstrip(')'))
        return list_to_return
    else:
        return [line.lstrip('contains ').rstrip(')')]


def create_dictionary(ingredients_and_allergens):
    allergy_dictionary = dict()
    for line in ingredients_and_allergens:
        separation_1 = line.split(' (')
        ingredients = separation_1[0].split()
        allergens = create_clean_dictionary_names(separation_1[1])
        for allergen in allergens:
            if allergen in allergy_dictionary.keys():
                for ingredient in ingredients:
                    allergy_dictionary[allergen].append(ingredient)
            else:
                allergy_dictionary[allergen] = []
                for ingredient in ingredients:
                    allergy_dictionary[allergen].append(ingredient)
    return allergy_dictionary


if __name__ == "__main__":
    some_ingredients_and_allergens = grab_input('ref_input')
    the_dictionary = create_dictionary(some_ingredients_and_allergens)
    for key in the_dictionary.keys():
        print(key)
        print(Counter(the_dictionary[key]))
