import Data.Complex
import qualified Data.Text as T

figureOutDirection :: Num a => (Char, b) -> (Complex a, b)
figureOutDirection (dir, distance)
    | dir == 'L' = ((0:+1), distance)
    | otherwise = ((0:+ (-1)), distance)


splitDirDistance :: [a] -> (a, [a])
splitDirDistance x = (head x, tail x)

fixString x = (fst x, read (snd x):: Float)

splitStringOnCommas :: String -> [String]
splitStringOnCommas x = map T.unpack (map T.strip (T.split (==',') (T.pack x)))

getComplexDirections :: Num a => String -> [(Complex a, Float)]
getComplexDirections x = map figureOutDirection (map fixString ((map splitDirDistance (splitStringOnCommas x))))

--move :: Num b => (b, b) -> (b, b) -> (b, b)
move (current_direction, location) (rotate, distance) = (current_direction * rotate, location + (current_direction * rotate * (distance:+0)))

finalLocation j = foldl move (0:+1, 0:+0) (getComplexDirections j)

finalAnswer x = abs (realPart (snd x)) + abs (imagPart (snd x))

-- finalAnswer (finalLocation "R2, L3")
    
main = do 
    let puzzleInput = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"
    print (finalAnswer (finalLocation puzzleInput))
