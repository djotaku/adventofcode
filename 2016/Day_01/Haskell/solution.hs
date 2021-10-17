import Data.Complex
import qualified Data.Text as T

figureOutDirection :: Num a => ([Char], b) -> (Complex a, b)
figureOutDirection (dir, distance)
    | dir == "L" = ((0:+1), distance)
    | otherwise = ((0:+ (-1)), distance)


splitDirDistance x = (head x, tail x)

splitStringOnCommas :: String -> [String]
splitStringOnCommas x = map T.unpack (map T.strip (T.split (==',') (T.pack x)))
    

