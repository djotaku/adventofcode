require "../../input_parsing/parse_input"

assembly = input_per_line('../input.txt')
pointer = 0
register_a = 1
register_b = 0
while pointer < assembly.length
  current_instruction = assembly[pointer].split
  if current_instruction.length ==2
    case current_instruction[0]
    when "hlf"
      case current_instruction[1]
      when "a"
        register_a = register_a / 2
        pointer += 1
      when "b"
        register_b = register_b / 2
        pointer += 1
      end
    when "tpl"
      case current_instruction[1]
      when "a"
        register_a *= 3
        pointer += 1
      when "b"
        register_b += 3
        pointer += 1
      end
    when "inc"
      case current_instruction[1]
      when "a"
        register_a += 1
        pointer += 1
      when "b"
        register_b += 1
        pointer += 1
      end
    when "jmp"
      pointer += current_instruction[1].to_i
    end
  else
    case current_instruction[0]
    when "jie"
      register_to_check = current_instruction[1].chop
      case register_to_check
      when "a"
        if register_a % 2 == 0
          pointer += current_instruction[2].to_i
        else
          pointer += 1
        end
      when "b"
        if register_b % 2 == 0
          pointer += current_instruction[2].to_i
        else
          pointer += 1
      end
      end
    when "jio"
      register_to_check = current_instruction[1].chop
      case register_to_check
      when "a"
        if register_a == 1
          pointer += current_instruction[2].to_i
        else
          pointer += 1
        end
      when "b"
        if register_b == 1
          pointer += current_instruction[2].to_i
        else
          pointer += 1
        end
      end
    end
  end
end



puts "The value in register b is #{register_b}"