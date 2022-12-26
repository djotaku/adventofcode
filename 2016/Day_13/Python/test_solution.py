from . import solution

def test_binary_representation():
    assert solution.binary_representation(2) == [1, 0]
    assert solution.binary_representation(3) == [1, 1]
    assert solution.binary_representation(4) == [1, 0, 0]

def test_wall_or_space():
    assert solution.wall_or_space(1, 0, 10) is False