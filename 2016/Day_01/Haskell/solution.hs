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


finalAnswer j = scanl (\x (y, z) -> (x * y), z) (0:+1) (getComplexDirections j)
