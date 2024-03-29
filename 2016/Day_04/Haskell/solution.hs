--Solution for Advent of Code 2016 Day 04 - Security Through Obscurity

import Data.Map as M
import Data.List as L
import qualified Data.Text as T

--read from a file and put array where each line is an element. Point free.
readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile 

--gives me a list of tuples (letter, frequency)
countCharacterFrequency x = M.toList $ M.fromListWith (+) [(c, 1) | c <- x]

--remove the hyphens from the string
removeHyphens xs = [ x | x <- xs, not (x `elem` "-") ]

-- helps us do first a sort by frequency and then alphabetical for ties
sortFreq (char1, freq1) (char2, freq2)
    | freq1 < freq2 = GT
    | freq1 > freq2 = LT
    | freq1 == freq2 =  compare char1 char2

    
    
--L.sortBy sortFreq (countCharacterFrequency "happy")


--sortBy sortFreq (countCharacterFrequency (removeHyphens (T.unpack (T.dropEnd 10 (T.pack "aaaaa-bbb-z-y-x-123[abxyz]")))))
