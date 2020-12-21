from . import solution_1


def test_grab_input():
    assert solution_1.grab_input('ref_input') == ["mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
                                                  'trh fvjkl sbzzf mxmxvkd (contains dairy)',
                                                  'sqjhc fvjkl (contains soy)', 'sqjhc mxmxvkd sbzzf (contains fish)']


def test_create_clean_dictionary_names():
    line = 'contains dairy, fish)'
    assert solution_1.create_clean_dictionary_names(line) == ['dairy', 'fish']


def test_create_dictionary():
    ingredients_and_allergens = ["mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
                                 'trh fvjkl sbzzf mxmxvkd (contains dairy)', 'sqjhc fvjkl (contains soy)',
                                 'sqjhc mxmxvkd sbzzf (contains fish)']
    allergy_dictionary = solution_1.create_dictionary(ingredients_and_allergens)
    assert allergy_dictionary['dairy'] == ['mxmxvkd', 'kfcds', 'sqjhc', 'nhms', 'trh', 'fvjkl', 'sbzzf', 'mxmxvkd']