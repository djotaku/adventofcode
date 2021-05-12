require 'json'
require "../../input_parsing/parse_input"


def json_sums(json_item)
    summation = 0
    if json_item.is_a?(Array)
        json_item.each do |item|
            summation += json_sums(item)
        end
    elsif json_item.is_a?(Integer)
        return json_item
    elsif json_item.is_a?(String)
        return 0
    else
        json_item.each_pair do |key, value|
            if json_item.values.include? 'red'
                return 0
            elsif value.is_a?(Integer)
                summation += value
            elsif value.is_a?(Array)
                summation += json_sums(value)
            elsif value.is_a?(Hash)
                summation += json_sums(value)
            else
                summation += 0
            end
        end
    end
    return summation
end

if $PROGRAM_NAME == __FILE__
    elf_json = input_per_line('../input.txt')
    parsed_elf_json = JSON.parse(elf_json[0])
    total = json_sums(parsed_elf_json)
    puts "The sum is #{total}"
end
