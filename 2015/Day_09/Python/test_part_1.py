from . import part_1


def test_parse_connections():
    one_set = ["London to Dublin = 464"]
    connection_dict = part_1.parse_connections(one_set)
    assert connection_dict["London"] == [{'Dublin': "464"}]


def test_traveling_salesman():
    example_graph = [[0, 464, 518, 0],
                     [464, 0, 141, 0],
                     [518, 141, 0, 0]]
    starting_city = 0
    assert(part_1.travelling_salesman_problem(example_graph, starting_city, 3)) == 605
