def determine_next_row_column(row, col)
  if row == 1
    new_row = col + 1
    new_col = 1
  else
    new_row = row - 1
    new_col = col + 1
  end
  [new_row, new_col]
end

def generate_next_code(previous_code)
  (previous_code * 252533) % 33554393
end

def algorithm_step(row, col, current_code)
  next_row, next_col = determine_next_row_column(row, col)
  next_code = generate_next_code(current_code)
  [next_row, next_col, next_code]
end

code = 27995004
row = 6
col = 6
while row != 2947 or col != 3029
  row, col, code = algorithm_step(row, col, code)
end

puts "The code at row: #{row}, col: #{col} is #{code}"