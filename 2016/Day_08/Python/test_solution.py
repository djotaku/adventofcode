from collections import defaultdict
from . import solution


def test_rect():
    test_display = defaultdict(int)
    assert test_display[(0, 0)] == 0
    assert test_display[(0, 1)] == 0
    assert test_display[(1, 1)] == 0
    assert test_display[(1, 0)] == 0
    test_display = solution.rect(test_display, 1, 1)
    assert test_display[(0, 0)] == 1
    assert test_display[(0, 1)] == 0
    assert test_display[(1, 1)] == 0
    assert test_display[(1, 0)] == 0
    test_display = solution.rect(test_display, 2, 2)
    assert test_display[(0, 0)] == 1
    assert test_display[(0, 1)] == 1
    assert test_display[(1, 1)] == 1
    assert test_display[(1, 0)] == 1
    test_display = solution.rect(test_display, 3, 2)
    assert test_display[(0, 0)] == 1
    assert test_display[(1, 0)] == 1
    assert test_display[(2, 0)] == 1
    assert test_display[(0, 1)] == 1
    assert test_display[(1, 1)] == 1
    assert test_display[(2, 1)] == 1


def test_rotate_row():
    test_display = defaultdict(int)
    test_display = solution.rect(test_display, 3, 2)
    assert test_display[(0, 0)] == 1
    assert test_display[(1, 0)] == 1
    assert test_display[(2, 0)] == 1
    test_display = solution.rotate_row(test_display, 0, 1, 4)
    assert test_display[(0, 0)] == 0
    test_display = solution.rotate_row(test_display, 0, 1, 4)
    assert test_display[(0, 0)] == 1
