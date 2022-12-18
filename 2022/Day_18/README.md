# Day 18 - Boiling Boulders

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/18).

## Part 1

## Part 2

## Commentary / Approach to the Problem
### Part 1
First attempt at figuring out an answer:
- Number of lines in input * 6 is the max number of sides
- I think each time a pair of points match, that's a side that matches so tally those up and and subtract from the above number. (Of course, the logic is in the tally)

That approach didn't really take into account the 3D space.

Second attempt: 

- Group cubes by Z-plane
- Test if cubes are touching on X-axis and remove 2 sides if they are
- Test if cubes are touching on Y-axis and remove 2 sides if they are

or simplify things? Put all cubes into a dict. Key is the coordinate. Test each cube to see if it's a neighbor with others. Do not test last cube or you'll get double-counts.
### Part 2
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
