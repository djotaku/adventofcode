from . import solution

def test_redistribute_blocks():
    block = [0, 2, 7, 0]
    assert solution.redistribute_blocks(block) == [2,4,1,2]