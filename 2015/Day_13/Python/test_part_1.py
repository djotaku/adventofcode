from . import part_1


def test_happy_seating_genetic_algorithm():
    # Alice, Bob, Carol, Dave
    seating_matrix = [[0, 54, -79, -2],
                      [83, 0, -7, -63],
                      [-62, 60, 0, 55],
                      [46, -7, 41, 0]]
    starting_person = 0
    assert part_1.happy_seating_genetic_algorithm(seating_matrix, starting_person, len(seating_matrix)) == 330


def test_create_dictionary():
    sentence = ["Alice would gain 54 happiness units by sitting next to Bob."]
    dictionary = part_1.create_dictionary(sentence)
    assert dictionary["Alice"]["Bob"] == '54'
    sentence = ["Alice would lose 79 happiness units by sitting next to Carol."]
    dictionary = part_1.create_dictionary(sentence)
    assert dictionary["Alice"]["Carol"] == '-79'


def test_create_graph():
    input_dictionary = {'Alice': {'Bob': 54, 'Carol': -79, 'Dave': -2},
                        'Bob': {'Alice': 83, 'Carol': -7, 'Dave': -63},
                        'Carol': {'Alice': -62, 'Bob': 60, 'Dave': 55},
                        'Dave': {'Alice': 46, 'Bob': -7, 'Carol': 41}}
    graph = part_1.create_graph(input_dictionary)
    assert graph == [[0, 54, -79, -2],
                    [83, 0, -7, -63],
                    [-62, 60, 0, 55],
                    [46, -7, 41, 0]]