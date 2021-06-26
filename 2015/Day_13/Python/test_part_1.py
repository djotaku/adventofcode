from . import part_1


def test_happy_seating_arrangement():
    # Alice, Bob, Carol, Dave
    seating_matrix = [[0, 54, -79, -2],
                      [83, 0, -7, -63],
                      [-62, 60, 0, 55],
                      [46, -7, 41, 0]]
    starting_person = 0
    assert part_1.happy_seating_arrangement(seating_matrix, starting_person, len(seating_matrix)) == 330
