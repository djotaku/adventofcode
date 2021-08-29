# Day 18: Like a GIF For Your Yard

ut of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/18).

## Part 1
Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:
```
1B5...
234...
......
..123.
..8A4.
..765.
```

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

- A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
- A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously; they all consider the same current state before moving to the next.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

Answer: 1061

## Part 2

## Commentary / Approach to the Problem
OK, this is this year's Conway's Game of Life problem. Since this is the first year of AoC this is a straight-forward GoL implementation - the standard rules.

Since I knew that there's usually a GoL problem each AoC year, I'd already watched a few videos on GoL strategy. 

So a few things I am thinking about going into this:

- Maybe convert all my hashes to 1s after import. This way I can simply sum up the neighbors to determine if a cell should live or die
- Question is whether I consider creating a grid (made of lists) or use a dictionary to only store the live cells. Dictionary uses less memory, but I think will require a bit more thinking to deal with lights that are off.

Depending on what I learn doing this, I will come back here and update this section after attempting to solve this problem.


## What I Learned

### Generic

### Python

### Ruby

### Perl

