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

move :: Num b => (b, b) -> (b, b) -> (b, b)
move (current_direction, location) (rotate, distance) = (current_direction * rotate, location + (current_direction * distance))

--finalAnswer j = scanl move (0:+1, 0:+0) (getComplexDirections j)
