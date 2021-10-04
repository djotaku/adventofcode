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

And that turned out to be the right answer. 
## What I Learned

### Generic

### Python
- Nothing
### Ruby

### Perl

### Go (Golang)

### Haskell
