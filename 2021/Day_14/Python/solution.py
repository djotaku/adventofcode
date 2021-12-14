"""Solution for Advent of Code 2021 Day 14: Extended Polymerization"""
from collections import defaultdict, Counter
import re
import logging
logger_14 = logging.getLogger("Day_14")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_per_line_unique_first_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        our_input = input_file.read()
        first_line, *rest_of_lines = our_input.split("\n")
        return first_line, rest_of_lines[1:]  # get rid of space as first element


def find_template_pairs(template: str) -> list:
    """"Take in the template file and return a list of pairs in the template"""
    template_as_letters = [letter for letter in template]
    return [template_as_letters[n]+template_as_letters[n+1] for n in range(len(template_as_letters)-1)]


def create_pair_insertion_dict(rules: str) -> dict:
    """Take in our insertion rules and create a dictionary of the rules."""
    regex = re.compile(r'(\w\w) -> (\w)')
    rule_dict = {}
    for rule in rules:
        this_rule = re.findall(regex, rule)
        rule_dict[this_rule[0][0]] = this_rule[0][1]
    return rule_dict


def transformation_step(before_dict: dict, rule_dict: dict) -> dict:
    """Take in a dictionary, transform it, return the new one.

    :param before_dict: A dictionary with the state of the molecule before the step is taken
    :param rule_dict: A dictionary with the rules for transformation
    :return: A dictionary with the new state of the molecule
    """


def transformation_step_2(list_of_pairs, rule_dict):
    new_pairs = []
    for pair in list_of_pairs:
        insertion_letter = rule_dict[pair]
        letters = [letter for letter in pair]
        new_pairs.append(letters[0]+insertion_letter)
        new_pairs.append(insertion_letter+letters[1])
    return new_pairs


def recreate_molecule(list_of_pairs) -> str:
    molecule = list_of_pairs[0]
    for pair in list_of_pairs[1:]:
        letters = [letter for letter in pair]
        molecule += letters[1]
    return molecule


if __name__ == "__main__":
    template_molecule, rules_for_transformation = input_per_line_unique_first_line("../input.txt")
    transformation_rules = create_pair_insertion_dict(rules_for_transformation)
    first_round_pairs = find_template_pairs(template_molecule)
    logger_14.debug(first_round_pairs)
    after_round_one = transformation_step_2(first_round_pairs, transformation_rules)
    logger_14.debug(f"{after_round_one=}")
    pairs = first_round_pairs
    for number in range(10):
        logger_14.debug(f"This is after step {number + 1}")
        pairs = transformation_step_2(pairs, transformation_rules)
        logger_14.debug(pairs)
    molecule_to_check = recreate_molecule(pairs)
    logger_14.debug(f"{molecule_to_check=}")
    logger_14.debug(f"{len(molecule_to_check)=}")
    letter_count = Counter(molecule_to_check)
    logger_14.debug(letter_count)
    letter_values = [value for value in letter_count.values()]
    letter_values.sort()
    logger_14.debug(letter_values)
    print(f"Difference between most common and least common letter is {letter_values[-1]-letter_values[0]}")
