"""Test Solution to Advent of Code Day 08: Seven Segment Search"""
from . import solution


def test_decode_segments():
    sample = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
    decoded_dict = solution.decode_segments(sample)
    print(decoded_dict)
    assert decoded_dict["cdfbe"] == 5