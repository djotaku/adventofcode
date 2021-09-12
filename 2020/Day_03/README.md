# Day 3: Toboggan Trajectory

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/3).

## Part 1

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many hashes would you encounter?

Answer: 191 

## Part 2

traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 hash(es) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of hashes encountered on each of the listed slopes?

Answer: 1478615040 

## Commentary / Approach to the Problem
When I did this with Python in 2020 (during AoC) I didn't use modulo, but I was pretty sure the problem had to do with modulo since it was a repeating pattern. 

For part 2, I did use some modulos.

You can see in my Python solution that I wasn't yet using unit tests, so I had print statements throughout both solutions to check the answers. 

## What I Learned

### Generic

### Python
- Nothing

### Ruby

### Perl
