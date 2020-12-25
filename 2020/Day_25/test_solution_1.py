from . import solution_1


def test_find_loop_size():
    public_key = 5764801
    assert solution_1.find_loop_size(public_key) == 8


def test_find_encryption_key():
    door_public_key = 17807724
    card_loop_size = 8
    assert solution_1.find_encryption_key(door_public_key, card_loop_size) == 14897079
