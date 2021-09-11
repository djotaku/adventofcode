require "../../input_parsing/parse_input"

require 'set'

def generate_molecule_tuple(list_of_molecules)
  list_of_molecules.map! {|line| [line.match(/(\w+) => (\w+)/).to_a[1], line.match(/(\w+) => (\w+)/).to_a[2]]}
end

def generate_replacements(string_to_replace, replace_with_string, molecule)
  matches = molecule.to_enum(:scan, string_to_replace).map { Regexp.last_match}
  matches.map{|molecule_match| molecule_match.pre_match + replace_with_string + molecule_match.post_match}
end

if $PROGRAM_NAME == __FILE__
  list_of_molecules = input_per_line('../input.txt')
  molecule_to_change = list_of_molecules.pop
  list_of_molecules.pop
  molecule_tuples = generate_molecule_tuple(list_of_molecules)
  list_of_potential_replacements = molecule_tuples.map {|item| generate_replacements(item[0], item[1],
                                                                                      molecule_to_change)}
  print list_of_potential_replacements
end
