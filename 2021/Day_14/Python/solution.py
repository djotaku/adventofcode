"""Solution for Advent of Code 2021 Day 14: Extended Polymerization"""
from collections import defaultdict, Counter
import re
import logging
logger_14 = logging.getLogger("Day_14")
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


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


def transformation_step(before_dict: dict, rule_dict: dict, this_letter_count: dict) -> (dict, dict):
    """Take in a dictionary, transform it, return the new one.

    :param this_letter_count: a count of all the letters in the polymer
    :param before_dict: A dictionary with the state of the molecule before the step is taken
    :param rule_dict: A dictionary with the rules for transformation
    :return: A dictionary with the new state of the molecule
    """
    new_dict = defaultdict(int)
    for pair, value in before_dict.items():
        insertion_letter = rule_dict[pair]
        letters = [letter for letter in pair]
        new_dict[letters[0]+insertion_letter] += before_dict[pair]
        new_dict[insertion_letter+letters[1]] += value
        this_letter_count[insertion_letter] += before_dict[pair]
    return new_dict, this_letter_count


if __name__ == "__main__":
    template_molecule, rules_for_transformation = input_per_line_unique_first_line("../input.txt")
    transformation_rules = create_pair_insertion_dict(rules_for_transformation)
    first_round_pairs = find_template_pairs(template_molecule)
    letter_count = Counter(template_molecule)
    logger_14.debug(f"{letter_count}")
    molecule_dict = Counter(first_round_pairs)
    part_1_letter_count = {}
    for number in range(40):
        logger_14.debug(f"This is after step {number + 1}")
        molecule_dict, letter_count = transformation_step(molecule_dict, transformation_rules, letter_count)
        logger_14.debug(f"{letter_count}")
        if number == 9:
            part_1_letter_count = letter_count.copy()
    part_1_answer = max(part_1_letter_count.values()) - min(part_1_letter_count.values())
    part_2_answer = max(letter_count.values()) - min(letter_count.values())
    print(f"Difference between most common and least common letter after 10 rounds is"
          f" {part_1_answer}.")
    print(f"Difference between most common and least common letter after 40 rounds is"
          f" {part_2_answer}.")