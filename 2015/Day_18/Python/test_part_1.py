from . import part_1

sample_initial_state_dictionary = {(0, 1): 1, (0, 3): 1, (0, 5): 1, (1, 3): 1, (1, 4): 1, (2, 0): 1,
                                   (2, 5): 1, (3, 2): 1, (4, 0): 1, (4, 2): 1, (4, 5): 1, (5, 0): 1,
                                   (5, 1): 1, (5, 2): 1, (5, 3): 1}


def test_new_status():
    assert part_1.new_status((0, 1), sample_initial_state_dictionary) == 0
    assert part_1.new_status((0, 0), sample_initial_state_dictionary) == 0
    assert part_1.new_status((1, 2), sample_initial_state_dictionary) == 1


def test_play_round():
    round_1 = part_1.play_round(6, sample_initial_state_dictionary)
    assert round_1[(0, 2)] == 1
    assert round_1[(0, 3)] == 1
    assert round_1[(1, 2)] == 1
    assert round_1[(1, 3)] == 1
    round_2 = part_1.play_round(6, round_1)
    assert round_2[(0, 0)] == 0
    assert round_2[(0, 1)] == 0
    assert round_2[(0, 2)] == 1
    assert round_2[(0, 3)] == 1
    assert round_2[(0, 4)] == 1
    assert round_2[(0, 5)] == 0


def test_initialize_board():
    test_board = [".#.#.#",
                  "...##.",
                  "#....#",
                  "..#...",
                  "#.#..#",
                  "####.."]
    assert part_1.initialize_board(test_board) == sample_initial_state_dictionary
