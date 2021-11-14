import Data.List

--read from a file and put array where each line is an element. Point free.
readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile 

-- Check 3 values to see if they make a valid triangle
validateTriangle :: (Ord a, Num a, Num p) => [a] -> p
validateTriangle [side1, side2, side3]
    | (side1 + side2 > side3) && (side1 + side3 > side2) && (side2 + side3 > side1) = 1
    | otherwise = 0

-- Take in a string of 3 numbers and run validateTriangle on it
evaluateTriple :: Num p => String -> p
evaluateTriple triple = validateTriangle (map (read::String->Int) (words triple))

checkAllPart1Triples :: Num b => [String] -> b
checkAllPart1Triples triples = sum (map evaluateTriple triples)

main = do
    ourInput <- readLines "../input.txt"
    print "The answer to part 1 is:"
    print (checkAllPart1Triples ourInput)
    --print (map words ourInput)
