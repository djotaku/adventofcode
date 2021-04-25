from dataclasses import dataclass


@dataclass
class Edge:
    """Stores an Edge"""
    vertex_1: str
    vertex_2: str
    distance: int

    def get_edge(self):
        return self.vertex_1, self.vertex_2, self.distance


class Graph:
    def __init__(self, edges):
        self.edges = [Edge(vert_1, vert_2, distance) for vert_1, vert_2, distance in edges]
        self.vertices = set()
        for edge in self.edges:
            self.vertices.add(edge.vertex_1)
            self.vertices.add(edge.vertex_2)

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.vertex_1].add((edge.vertex_2, edge.distance))

        return neighbours


def find_shortest_route_to_all_destinations(graph: Graph) -> int:
    routes = []
    vertex_dict = graph.neighbours
    for vertex in graph.vertices:
        need_to_visit = graph.vertices.pop(vertex)


if __name__ == "__main__":
    graph = Graph([("London", "Dublin", 464), ("London", "Belfast", 548), ("Dublin", "Belfast", 141)])
    neighbors = graph.neighbours
    print(neighbors["London"])
    print(neighbors["Dublin"])