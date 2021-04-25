from . import part_1


def test_hamilton_wak():
    flight_connections = {"London": ["Dublin", "Belfast"], "Dublin": ["Belfast", "London"],
                          "Belfast": ["London", "Dublin"]}
    assert part_1.hamilton_walk(flight_connections, "London") == ['London', 'Belfast', 'Dublin']  # 659
    assert part_1.hamilton_walk(flight_connections, "Dublin") == ['Dublin', 'London', 'Belfast']  # 982
    assert part_1.hamilton_walk(flight_connections, "Belfast") == ['Belfast', 'London', 'Dublin']  # 982


def test_parse_connections():
    one_set = ["London to Dublin = 464"]
    connection_dict = part_1.parse_connections(one_set)
    assert connection_dict["London"] == [{'Dublin': "464"}]
