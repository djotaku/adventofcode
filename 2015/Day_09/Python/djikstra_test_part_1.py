from . import dijkstra_part_1


def test_dijkstra():
    graph = dijkstra_part_1.Graph([("London", "Dublin", 464), ("London", "Belfast", 518), ("Dublin", "Belfast", 141)])
    answer = graph.dijkstra("London", "Belfast")
    assert list(answer) == ["London", "Dublin", "Belfast"]
