require "../../input_parsing/parse_input"

require 'set'

def generate_molecule_tuple(list_of_molecules)
  list_of_molecules.map! {|line| [line.match(/(\w+) => (\w+)/).to_a[1], line.match(/(\w+) => (\w+)/).to_a[2]]}
end


if $PROGRAM_NAME == __FILE__
  list_of_molecules = input_per_line('../input.txt')
  molecule_to_change = list_of_molecules.pop
  list_of_molecules.pop
  print generate_molecule_tuple(list_of_molecules)
end
