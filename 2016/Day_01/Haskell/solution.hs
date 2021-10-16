import Data.Complex

figureOutDirection :: Num a => ([Char], b) -> (Complex a, b)
figureOutDirection (dir, distance)
    | dir == "L" = ((0:+1), distance)
    | otherwise = ((0:+ (-1)), distance)
