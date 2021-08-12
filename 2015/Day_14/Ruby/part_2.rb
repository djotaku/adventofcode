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

if $PROGRAM_NAME == __FILE__
  reindeer_lineup = input_per_line('../input.txt')

end