require "../../input_parsing/parse_input"

class Reindeer
  def initialize(speed, flying_time, resting_time)
    @speed = speed
    @flying_time = flying_time
    @original_flying_time = flying_time
    @resting_time = resting_time
    @original_resting_time = resting_time
    @total_distance = 0
    @points = 0
  end

  def total_distance
    @total_distance
  end

  def add_a_point
    @points += 1
  end

  def move
    if @resting_time == 0
      @flying_time = @original_flying_time
      @resting_time = @original_resting_time
    end
    if @flying_time > 0
      @total_distance += @speed
      @flying_time -= 1
    elsif @resting_time > 0
      @resting_time-= 1
    end
  end
end


def get_reindeer_specs(line)
  line.scan(/(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds./)
end


def move_and_assign_points(list_of_reindeer, total_seconds)
  time = 0
  while time < total_seconds + 1
    list_of_reindeer.each do | reindeer|
      reindeer.move()
    end
    list_of_reindeer = list_of_reindeer.sort { |a, b| a.total_distance <=> b.total_distance }
    current_top_distance = list_of_reindeer[-1].total_distance
    list_of_reindeer.each do | reindeer|
      if reindeer.total_distance == current_top_distance
        reindeer.add_a_point
      end
    end
  end
end


if $PROGRAM_NAME == __FILE__
  reindeer_lineup = input_per_line('../input.txt')
  reindeer_list = []
  reindeer_lineup.each do |reindeer|
    reindeer_info = get_reindeer_specs(reindeer)
    reindeer_list.append(Reindeer.new(reindeer_info[0][1].to_i, reindeer_info[0][2].to_i, reindeer_info[0][3].to_i))
  end
  move_and_assign_points(reindeer_list, 2503)
end