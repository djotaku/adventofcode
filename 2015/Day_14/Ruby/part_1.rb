require "../../input_parsing/parse_input"


def reindeer_distance(speed, flying_time, resting_time, total_time)
    remaining_time = total_time
    flown_distance = 0
    while remaining_time > 0 do
        if remaining_time >= flying_time
            flown_distance += speed * flying_time
            remaining_time -= flying_time
        else
            flown_distance += speed * remaining_time
            remaining_time = 0
        end
        if remaining_time >= resting_time
            remaining_time -= resting_time
        else
            remaining_time = 0
        end
    end
    flown_distance
end


def get_reindeer_specs(line)
    line.scan(/(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds./)
end

if $PROGRAM_NAME == __FILE__
    reindeer_list = input_per_line('../input.txt')
    longest_distance = 0
    reindeer_list.each do | reindeer |
        reindeer_info = get_reindeer_specs(reindeer)
        distance = reindeer_distance(reindeer_info[0][1].to_i, reindeer_info[0][2].to_i, reindeer_info[0][3].to_i, 2503)
        if distance > longest_distance
            longest_distance = distance
        end
    end
    puts "Fastest reindeer went #{longest_distance} km."
end
