from collections import defaultdict
import solution


def test_create_next_row():
    test_floor_map = defaultdict(bool)
    test_floor_map[(0, 0)] = False
    test_floor_map[(0, 1)] = False
    test_floor_map[(0, 2)] = True
    test_floor_map[(0, 3)] = True
    test_floor_map[(0, 4)] = False
    new_floor_map = solution.create_next_row(test_floor_map, 1, 5)
    assert new_floor_map[(1, 0)] is False
    assert new_floor_map[(1, 1)] is True
    assert new_floor_map[(1, 2)] is True
    assert new_floor_map[(1, 3)] is True
    assert new_floor_map[(1, 4)] is True
