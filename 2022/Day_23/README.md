# Day 23 - Unstable Diffusion

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/23).

## Part 1

## Part 2

## Commentary / Approach to the Problem
### Part 1
- Since the empty space extends in all directions maybe can go for a defaultdict bool where True has an elf and False is empty (might even simplify some of the comparisons)
- Have a deque with the options of what an elf considers first and popleft, insert each round to make the next one the first option an elf considers
- For all elves
  - First if statement checks the 8 directions - maybe take a lesson from the BFS day and have 2 lists representing x and y one each. The lists are 0, -1, or 1. Then you can apply this math throughout in order to make keeping track of things easier.
  - Each elf checks their NSEW directions to determine whether or not to move
  - Need a list where elves put their proposed moves (how to keep this from ballooning during the check phase?)  OK, what if I make a dictionary of proposed moves? The keys are the positions we want to move to. The values are lists. If any list contains more than one elf in it, those elves don’t get to move. Dict resets each round. I think this is the cleanest way to to this.
  - Finally, after 10 turns (probably make this a variable because part 2 is after more turns?) create bounding box. Search dictionary for highest/lowest x and y. Probably most efficient is to have it go through its keys and for each value, check against x_high, x_low, y_high, y_low and update if necessary. Then you have your bounds. You can then iterate over those bounds to count up “False”s

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
    