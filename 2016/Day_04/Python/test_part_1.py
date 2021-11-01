from . import part_1

def test_is_real_room():
    room_one = "aaaaa-bbb-z-y-x-123[abxyz]"
    assert part_1.is_real_room(room_one) == 123
    room_two = "a-b-c-d-e-f-g-h-987[abcde]"
    assert part_1.is_real_room(room_two) == 987
    room_three = "not-a-real-room-404[oarel]"
    assert part_1.is_real_room(room_three)
    room_four = "totally-real-room-200[decoy]"
    assert part_1.is_real_room(room_four)
