from . import solution


def test_is_real_room():
    room_one = "aaaaa-bbb-z-y-x-123[abxyz]"
    assert solution.is_real_room(room_one) == (123, 0)
    room_two = "a-b-c-d-e-f-g-h-987[abcde]"
    assert solution.is_real_room(room_two) == (987, 0)
    room_three = "not-a-real-room-404[oarel]"
    assert solution.is_real_room(room_three) == (404, 0)
    room_four = "totally-real-room-200[decoy]"
    assert solution.is_real_room(room_four) == (0, 0)


def test_decipher_and_discover():
    encrypted_room = ["qzmt", "zixmtkozy", "ivhz"]
    assert not solution.decipher_and_discover(encrypted_room, 343)
