import Data.List
import qualified Data.Text as T

-- given a number and a direction, give back the new number
findNextNumber :: (Eq a, Num a, Num p) => a -> Char -> p
findNextNumber number direction
    | (number == 1) && (direction == 'U') = 1
    | (number == 1) && (direction == 'D') = 4
    | (number == 1) && (direction == 'L') = 1
    | (number == 1) && (direction == 'R') = 2
    | (number == 2) && (direction == 'U') = 2
    | (number == 2) && (direction == 'D') = 5
    | (number == 2) && (direction == 'L') = 1
    | (number == 2) && (direction == 'R') = 3
    | (number == 3) && (direction == 'U') = 3
    | (number == 3) && (direction == 'D') = 6
    | (number == 3) && (direction == 'L') = 2
    | (number == 3) && (direction == 'R') = 3
    | (number == 4) && (direction == 'U') = 1
    | (number == 4) && (direction == 'D') = 7
    | (number == 4) && (direction == 'L') = 4
    | (number == 4) && (direction == 'R') = 5
    | (number == 5) && (direction == 'U') = 2
    | (number == 5) && (direction == 'D') = 8
    | (number == 5) && (direction == 'L') = 4
    | (number == 5) && (direction == 'R') = 6
    | (number == 6) && (direction == 'U') = 3
    | (number == 6) && (direction == 'D') = 9
    | (number == 6) && (direction == 'L') = 5
    | (number == 6) && (direction == 'R') = 6
    | (number == 7) && (direction == 'U') = 4
    | (number == 7) && (direction == 'D') = 7
    | (number == 7) && (direction == 'L') = 7
    | (number == 7) && (direction == 'R') = 8
    | (number == 8) && (direction == 'U') = 5
    | (number == 8) && (direction == 'D') = 8
    | (number == 8) && (direction == 'L') = 7
    | (number == 8) && (direction == 'R') = 9
    | (number == 9) && (direction == 'U') = 6
    | (number == 9) && (direction == 'D') = 9
    | (number == 9) && (direction == 'L') = 8
    | (number == 9) && (direction == 'R') = 9


-- take an array of instructions and a starting number and find the final number
findNumberRow :: (Foldable t, Eq a, Num a) => a -> t Char -> a
findNumberRow number directionList = foldl findNextNumber number directionList

--puting it all together
almostFinalAnswer :: (Foldable t, Eq b, Num b) => [t Char] -> [b]
almostFinalAnswer aocinput = scanl findNumberRow 5 aocinput

-- get rid of that extra first number
finalAnswer :: (Foldable t, Eq a, Num a) => [t Char] -> [a]
finalAnswer aocinput = tail (almostFinalAnswer aocinput)

--make it one string
stringFinalAnswer :: Foldable t => [t Char] -> [Char]
stringFinalAnswer aocinput = concat (map show (finalAnswer aocinput))

--read from a file and put array where each line is an element. Point free.
readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile 

main = do
    ourInput <- readLines "../input.txt"
    print "The answer to part 1 is:"
    print (stringFinalAnswer ourInput)
