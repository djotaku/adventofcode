# Day 09 - Rope Bridge

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/9).

## Part 1

Answer: 6197
## Part 2

Answer: 2562
## Commentary / Approach to the Problem
### Part 1
Seems like the keys are:
- Is Tail in the same row or column as Head? (Do they share x or y coordinates)
    - If yes, move straight
    - If no, move diagonally
- Are they touching? If so, do not need to move tail (includes diagonal checks)
- Need a Set to keep track of points visited so you count them only once

Since we're not given any initial map, just start at (0,0) with head on tail 

### Part 2
My first thought was to create a list and have each considered as the head and tail.
I don't think that's horribly wrong, but the problem is that when you have more than one piece, you're not necessarily always moving in the same direction.

I think I need to set it up so that each piece that moves lets the next one know which direction it went so that it can follow in the right way.

That was a lot harder than I thought it would be!
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
