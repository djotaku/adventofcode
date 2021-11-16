require "../../input_parsing/parse_input"

def count_and_sort_letters(room_string)
  room_string.scan(/[a-z]/).tally.to_a.sort_by!{|character| [-character[1], character[0]]}[0..4]
end

def valid_sector_id(character_count, checksum)
  character_count.map.with_index { |character, index| character[0] == checksum[index]}.all?
end

encrypted_rooms = input_per_line("../input.txt")
sector_id_sum = 0
encrypted_rooms.each do |room|
  encrypted_part = room.scan(/(\w+-)/).join
  character_counts = count_and_sort_letters(encrypted_part)
  sector_and_checksum = room.scan(/(\d+)\[(\w+)\]/)
  if valid_sector_id(character_counts, sector_and_checksum[0][1])
    sector_id_sum += sector_and_checksum[0][0].to_i
  end
end

puts "The sum of the sector IDs of the real rooms: #{sector_id_sum}"

#for part 2
#  test = "abc".chars.each.map{|letter| letter.next}.join
#  better
#  test = "abc".chars.map{|letter| letter.next}.join
irb(main):053:1* def lettermove(letter, number)
irb(main):054:2*   (0..number).each do 
irb(main):055:2*     letter = letter.next
irb(main):056:1*   end
irb(main):057:1*   letter
irb(main):058:0> end


