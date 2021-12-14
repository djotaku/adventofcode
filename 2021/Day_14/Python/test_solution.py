"""Test solution for Advent of Code 2021 Day 14: Extended Polymerization"""
from . import solution

template_molecule, rules_for_transformation = solution.input_per_line_unique_first_line("../test_input.txt")


def test_find_template_pairs():
    pairs = solution.find_template_pairs(template_molecule)
    assert pairs == ["NN", "NC", "CB"]


def test_rule_dict_creation():
    rule_dict = solution.create_pair_insertion_dict(rules_for_transformation)
    assert rule_dict["CH"] == "B"
    assert rule_dict["NC"] == "B"


def test_transformation_step_2():
    pairs = ["NN", "NC", "CB"]
    rule_dict = solution.create_pair_insertion_dict(rules_for_transformation)
    new_pairs = solution.transformation_step_2(pairs, rule_dict)
    check_pairs = solution.find_template_pairs("NCNBCHB")
    assert sorted(new_pairs) == sorted(check_pairs)
