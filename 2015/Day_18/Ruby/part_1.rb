require "../../input_parsing/parse_input"

def initialize_board(list_of_rows)
  board = Hash.new
  list_of_rows.each_with_index do |row, row_index |
    columns = row.split(//)
    columns.each_with_index do |column, column_index|
      if column == "#"
        board[[row_index, column_index]] = 1
      end
    end
  end
  return board
end

def new_status(coordinate, board)
  live_neighbors = 0
  alive = board[coordinate]
  if board[[coordinate[0]-1, coordinate[1]-1]] == 1
    live_neighbors += 1
  end
  if board[[coordinate[0], coordinate[1]-1]] == 1
    live_neighbors += 1
  end
  if board[[coordinate[0]+1, coordinate[1]-1]] == 1
    live_neighbors += 1
  end
  if board[[coordinate[0]+1, coordinate[1]]] == 1
    live_neighbors += 1
  end
  if board[[coordinate[0]+1, coordinate[1]+1]] == 1
    live_neighbors += 1
  end
  if board[[coordinate[0], coordinate[1]+1]] == 1
    live_neighbors += 1
  end
  if board[[coordinate[0]-1, coordinate[1]+1]] == 1
    live_neighbors += 1
  end
  if board[[coordinate[0]-1, coordinate[1]]] == 1
    live_neighbors += 1
  end
  if alive
    if (2..3).cover? live_neighbors
      return 1
    else
      return 0
    end
  end
  if not alive and live_neighbors == 3
    1
  end
end

def play_round(grid_size, board)
  new_board = Hash.new
  (0..grid_size).each do |x|
    (0..grid_size).each do |y|
      new_board[[x, y]] = new_status([x,y], board)
    end
  end
  new_board
end

if $PROGRAM_NAME == __FILE__
  day_18_input = input_per_line('../input.txt')
  initial_board = initialize_board(day_18_input)
  board = initial_board.compact
  (1..100).each {board = play_round(100, board)}
  puts "There are  lights #{board.values.sum} on."
end
