import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def generate_replacements(string_to_replace: str, replace_with_string: str, molecule: str):
    """Given a string to replace and a replacement string, replace each instance one by one.

    One by one constraint is why we can't just use Python's string.replace.
    """
    match = re.finditer(string_to_replace, molecule)
    return [molecule[0:m.start()] + replace_with_string + molecule[m.end():]
            for m in match]


def generate_molecule_tuple(list_of_molecules: list):
    regex = re.compile(r'(\w+) => (\w+)')
    molecule_tuple_list = []
    for item in list_of_molecules:
        molecules = re.findall(regex, item)
        molecule_tuple_list.append((molecules[0][0], molecules[0][1]))
    return molecule_tuple_list


if __name__ == "__main__":
    rudy_medicine_molecules = parse_input.input_per_line('../input.txt')
    molecule_to_change = rudy_medicine_molecules.pop()
    # one more pop for the newline between the list of molecules and the one to change
    rudy_medicine_molecules.pop()
    molecule_tuples = generate_molecule_tuple(rudy_medicine_molecules)
    distinct_molecules = set()
    for item in molecule_tuples:
        list_of_potential_replacements = generate_replacements(item[0], item[1], molecule_to_change)
        for potential_replacement in list_of_potential_replacements:
            distinct_molecules.add(potential_replacement)
    print(f"We have {len(distinct_molecules)} distinct molecules.")

