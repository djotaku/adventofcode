import System.IO
import Data.String

main= do
contents <- readFile "../numeric_per_line_input.txt"
putStr contents 
