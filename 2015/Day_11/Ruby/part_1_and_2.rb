def rule_one(password)
    characters = password.split(//)
    triple_straight = characters.chunk_while { |i, j| i.next == j }.filter{|chunk| chunk.length >= 3}
    triple_straight.length >= 1
end


def rule_two(password)
    !password.include? "i" and !password.include? "o" and !password.include? "l"
end


def rule_three(password)
    pairs = password.scan(/(\w)\1/)
    pairs.length >= 2
end

if $PROGRAM_NAME == __FILE__
    current_password = "hxbxwxba"
    puts "Santa's starting password is: #{current_password}"
    until rule_one(current_password) and rule_two(current_password) and rule_three(current_password)
        current_password = current_password.next
    end
    puts "Santa's next password should be: #{current_password}"
    puts "Then Santa's password expired again!"
    current_password = current_password.next
    until rule_one(current_password) and rule_two(current_password) and rule_three(current_password)
        current_password = current_password.next
    end
    puts "Santa's next password should be: #{current_password}"
end
