require_relative "part_1"
require 'test/unit'

class TestShortestHamiltonian < Test::Unit::TestCase
    
    def test_parse_connections
        one_set = ["London to Dublin = 464"]
        city_hash = parse_connections(one_set)
        assert_equal("464", city_hash["London"]["Dublin"])
        full_set = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]
        city_hash = parse_connections(full_set)
        assert_equal("464", city_hash["London"]["Dublin"])
        assert_equal("518", city_hash["London"]["Belfast"])
    end
    
    def test_create_matrix
        full_set = ["London to Dublin = 464", "London to Belfast = 518", "Dublin to Belfast = 141"]
        city_hash = parse_connections(full_set)
        matrix = create_matrix(city_hash)
        assert_equal([[0, 464, 518, 0], [464, 0, 141, 0], [518, 141, 0, 0], [0, 0, 0, 0]], matrix)
    end
    
    def test_traveling_salesman
        advent_of_code_example_graph = [[0, 464, 518, 0],
                                        [464, 0, 141, 0],
                                        [518, 141, 0, 0],
                                        [0, 0, 0, 0]]
        starting_city = 0
        assert_equal(605, traveling_salesman(advent_of_code_example_graph, starting_city, advent_of_code_example_graph.length))
    end
end
