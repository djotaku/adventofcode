require "../../input_parsing/parse_input"

def create_guest_hash(lines)
    guest_hash = Hash.new
    lines.each do | line |
        people_and_values = line.scan(/(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\./)
        if !guest_hash.has_key?(people_and_values[0][0])
            guest_hash[people_and_values[0][0]] = {}
        end
        number = people_and_values[0][1] == "lose" ? "-#{people_and_values[0][2]}" : "#{people_and_values[0][2]}"
        guest_hash[people_and_values[0][0]][people_and_values[0][3]] = number
    end
    guest_hash
end


def create_matrix(guest_hash)
    index_hash = Hash.new
    guest_hash.keys.each_with_index do | key, index |
        index_hash[index] = key
    end
    matrix = []
    index_hash.keys.each_with_index do |index|
        temp_internal_list = []
        current_person = index_hash[index]
        index_hash.keys.each_with_index do |internal_index|
            if internal_index == index
                temp_internal_list.append(0)
            else
                temp_internal_list.append(guest_hash[current_person][index_hash[internal_index]].to_i)
            end
        end
        matrix.append(temp_internal_list)
    end
    matrix
end


def perfect_seating(happiness_graph, starting_person, number_of_people)
    vertex = []
    (0...number_of_people).each do |number|
        if number != starting_person
            vertex.append(number)
        end
    end
    max_happiness = 0
    permutation_list = vertex.permutation.to_a
    permutation_list.each do |permutation|
        current_happiness_weight = 0
        
        outer_array_index = starting_person
        permutation.each do |inner_array_index|
            current_happiness_weight += happiness_graph[outer_array_index][inner_array_index]
            current_happiness_weight += happiness_graph[inner_array_index][outer_array_index]
            outer_array_index = inner_array_index
        end
        current_happiness_weight += happiness_graph[outer_array_index][starting_person]
        current_happiness_weight += happiness_graph[starting_person][outer_array_index]
        
        max_happiness = [max_happiness, current_happiness_weight].max
    end
    max_happiness
end


if $PROGRAM_NAME == __FILE__
    guest_preferences = input_per_line('../input.txt')
    guest_preference_hash = create_guest_hash(guest_preferences)
    guest_preference_matrix = create_matrix(guest_preference_hash)
    starting_person = 0
    total_happiness = perfect_seating(guest_preference_matrix, starting_person, guest_preference_matrix.length)
    puts "With the perfect seating arrangement total happiness is #{total_happiness}."
end
