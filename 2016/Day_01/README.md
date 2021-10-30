# Day 1: No Time for a Taxicab

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/1).

## Part 1
...you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

- Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
- R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
- R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

Answer: 146
## Part 2

Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

Answer: 131

## Commentary / Approach to the Problem
### Part 1
I knew the key was in his link. That took me to the taxicab distance. So I only had to solve for: (p1,p2) and (q1,q2)= |p1-q1| + |p2-q2| 

The most important part was keeping track of which direction I was facing.
### Part 2
[First I decided to store the coordinates in a set](https://github.com/djotaku/adventofcode/blob/e6c22e5425d60cbdd3f6dc21102469723d1d3f59/2016/Day_01/Python/part_2.py). But that didn't pass the example code.

[So I tried to do it based on magnitude, because that seemed to be the right answer.](https://github.com/djotaku/adventofcode/blob/dc15484945244957ff2c347d561c242b906fae22/2016/Day_01/Python/part_2.py)

Alas, that was not right either.

Then I had an epiphany, I think I had to keep track of my coordinates along the way, not just where I stop at the end of a direction. In other words for a north 4, I should see if I have previously stopped at (0,1), (0,2), (0,3), or (0, 4).

And [that turned out to be the right answer.](https://github.com/djotaku/adventofcode/blob/98c267c0ddbaafd4c057960b946fec9412621693/2016/Day_01/Python/part_2.py) However, my code was a bit messy. I'd like to see if I can clean things up a bit when I do the problem in the other languages.

I know the answer was in the careful reading of the problem, but boy was that one much trickier than it seemed to be at first!

### Post-Python

I knew intuitively that this needed to be simpler than tracking orientation. Something with polar coordinates. Since Haskell doesn’t track state, I was looking at AoC on reddit to see if there was someone who could explain how to do this without keeping state and found [this post](https://www.reddit.com/r/adventofcode/comments/5fur6q/comment/dangjvv/?utm_source=share&utm_medium=web2x&context=3). That’s it! Using complex numbers should make this work. So I decided to not look at that answer again, but use the idea of complex numbers in the Ruby, Perl, Go, and Haskell solutions. Also to maybe design with part 2 in mind. And that's how I did the Ruby solution. For my first Ruby attempt, I tried to use coordinates rather than complex numbers based on the following from Wikipedia: (a+bi) * i = ai + b(i^2) = -b + ai but I couldn't get the right answer. Then it turned out that I was doing something slightly wrong in my regex check, so I may try to use that principle again in Perl, Go, and/or Haskell rather than relying on Complex numbers. That said, it wasn't the end of the world to use complex numbers. 

With Perl I made it work without using Complex numbers. Key was the realization that I needed a temp variable to hold direction[0] in order to be able to transfer it over to direction[y].

## What I Learned

### Generic
- Using complex numbers when there's an AoC problem involving rotating on the cardinal directions.

### Python
- Nothing
### Ruby
- How to use Complex numbers in Ruby
### Perl
- Nothing new
### Go (Golang)
- First go program ever other than Hello World type program
- Learned how to use arrays and slices
- how to do regular expressions in Go. For the compile want to use back-tick
- strconv.Atoi to make strings into integers
- strconv.Itoa to make ints into strings!
### Haskell
SO, SO MUCH!!
- Writing functions in Haskell
- using head and tail to split an array
- using fst and snd to get the first and second items in an array or tuple
- using map in Haskell
- Using Data.Text to format the data into a usable format
- putting a bunch of functions back to back to get an answer
- How to use main
- how to compile Haskell
- How to have named inputs to functions and how to use them
