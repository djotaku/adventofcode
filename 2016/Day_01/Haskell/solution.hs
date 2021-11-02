import Data.Complex
import qualified Data.Text as T

-- Using the polar math turn one direction if L and the other way if R (or anything, but we know it'll be R)
figureOutDirection :: Num a => (Char, b) -> (Complex a, b)
figureOutDirection (dir, distance)
    | dir == 'L' = ((0:+1), distance)
    | otherwise = ((0:+ (-1)), distance)

-- This splits the letter from the number in the input
splitDirDistance :: [a] -> (a, [a])
splitDirDistance x = (head x, tail x)

-- this converts the number from a string into a Float number
fixString x = (fst x, read (snd x):: Float)

-- First convert the string into a Data.Text, split on the commas, then turn back into a string.
splitStringOnCommas :: String -> [String]
splitStringOnCommas x = map T.unpack (map T.strip (T.split (==',') (T.pack x)))

-- Basically we convert the puzzle input into a series of complex numbers and distances
getComplexDirections :: Num a => String -> [(Complex a, Float)]
getComplexDirections x = map figureOutDirection (map fixString ((map splitDirDistance (splitStringOnCommas x))))

--move :: Num b => (b, b) -> (b, b) -> (b, b)
-- does the actual movement along the blocks one block at a time.
move (current_direction, location) (rotate, distance) = (current_direction * rotate, location + (current_direction * rotate * (distance:+0)))

-- foldl to apply the move across the entire series of directions
finalLocation j = foldl move (0:+1, 0:+0) (getComplexDirections j)

-- now that we know where we ended up, take the absolute values of the final coordinates and sum. 
finalAnswer x = abs (realPart (snd x)) + abs (imagPart (snd x))

-- finalAnswer (finalLocation "R2, L3")
    
main = do 
    let puzzleInput = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"
    print (finalAnswer (finalLocation puzzleInput))
