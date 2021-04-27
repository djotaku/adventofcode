require "../../input_parsing/parse_input"


def parse_connections(lines)
    city_connection_hash = Hash.new
    lines.each do |line|
        destinations = line.scan(/(\w+) to (\w+) = (\d+)/)
        if !city_connection_hash.has_key?(destinations[0][0])
            city_connection_hash[destinations[0][0]] = {}
        end
        city_connection_hash[destinations[0][0]][destinations[0][1]] = destinations[0][2]
        if !city_connection_hash.has_key?(destinations[0][1])
            city_connection_hash[destinations[0][1]] = {}
        end
        city_connection_hash[destinations[0][1]][destinations[0][0]] = destinations[0][2]
    end
    city_connection_hash
end


def create_matrix(city_hash)
    index_hash = Hash.new
    city_hash.keys.each_with_index do |key, index|
        index_hash[index] = key
    end
    matrix = []
    index_hash.keys.each_with_index do |index|
        temp_internal_list = []
        current_city = index_hash[index]
        index_hash.keys.each_with_index do |internal_index|
            if internal_index == index
                temp_internal_list.append(0)
            else
                temp_internal_list.append(city_hash[current_city][index_hash[internal_index]].to_i)
            end
        end
        temp_internal_list.append(0)
        matrix.append(temp_internal_list)
    end
    final_zeroes = [0] * (index_hash.length + 1) 
    matrix.append(final_zeroes)
    matrix
end

def traveling_salesman(graph, starting_city, number_of_cities)
    vertex = []
    (0...number_of_cities).each do |number|
        if number != starting_city
            vertex.append(number)
        end
    end
    min_path = 10000000000000000000000000 # super huge number
    permutation_list = vertex.permutation.to_a
    permutation_list.each do |permutation|
        current_path_weight = 0
        
        outer_array_index = starting_city
        permutation.each do |inner_array_index|
            current_path_weight += graph[outer_array_index][inner_array_index]
            outer_array_index = inner_array_index
        end
        current_path_weight += graph[outer_array_index][starting_city]
        
        min_path = [min_path, current_path_weight].min
    end
    min_path
end


if $PROGRAM_NAME == __FILE__
    city_list = input_per_line('../input.txt')
    city_connections = parse_connections(city_list)
    city_matrix = create_matrix(city_connections)
    starting_city = 0
    distance = traveling_salesman(city_matrix, starting_city, city_matrix.length)
    puts "To visit each city only once, Santa must travel #{distance} miles."
end
