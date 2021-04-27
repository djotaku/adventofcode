from . import part_1


def test_parse_connections():
    one_set = ["London to Dublin = 464"]
    connection_dict = part_1.parse_connections(one_set)
    assert connection_dict["London"] == {'Dublin': "464"}
    assert connection_dict["Dublin"] == {'London': "464"}
    full_set = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]
    connection_dict = part_1.parse_connections(full_set)
    assert connection_dict["London"] == {'Dublin': "464", "Belfast": "518"}


def test_traveling_salesman():
    advent_of_code_example_graph = [[0, 464, 518, 0],
                                    [464, 0, 141, 0],
                                    [518, 141, 0, 0],
                                    [0, 0, 0, 0]]
    starting_city = 0
    assert(part_1.travelling_salesman_problem(advent_of_code_example_graph, starting_city, 4)) == 605
    website_example_graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    assert(part_1.travelling_salesman_problem(website_example_graph, 0, 4)) == 80


def test_create_matrix():
    full_set = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]
    connection_dict = part_1.parse_connections(full_set)
    matrix = part_1.create_matrix(connection_dict)
    assert matrix == [[0, 464, 518, 0], [464, 0, 141, 0], [518, 141, 0, 0], [0, 0, 0, 0]]
