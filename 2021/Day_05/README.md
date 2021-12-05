# Day 5: Hydrothermal Venture

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/5).

## Part 1
For example:

    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

- An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
- An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

you need to determine the number of points where at least two lines overlap.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1
My initial strategy is to:
- Parse each line of the input to figure out the points it crosses
- Use the Counter to count how many points are 2 or larger
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
