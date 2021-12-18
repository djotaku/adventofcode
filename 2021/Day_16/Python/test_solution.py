"""Test solution for Day 16: Packet Decoder"""
from . import solution


def test_hex_to_binary():
    binary = solution.hex_to_binary("D2FE28")
    assert binary == "110100101111111000101000"


def test_read_subpacket():
    binary_subpacket = "110100101111111000101000"
    fields = solution.read_subpacket(binary_subpacket)
    assert fields["version"] == 6
    assert fields["packet_type"] == 4
    assert fields["literal number"] == 2021


def test_type_0():
    binary_subpacket = solution.hex_to_binary("38006F45291200")
    fields = solution.read_subpacket(binary_subpacket)
    assert fields["version"] == 1
    assert fields["packet_type"] == 6
    assert fields["length type"] == "0"
    # still need to write test to make sure subpackets are recording correctly
