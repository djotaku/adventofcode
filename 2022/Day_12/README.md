# Day 12 - Hill Climbing Algorithm

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/12).

## Part 1

Answer: 520

## Part 2

Answer: 508

## Commentary / Approach to the Problem
### Part 1
I'm not good at these, I never know how to actually do it. I know that, generally, it's something like:

- figure out every direction you can go from your current spot
- branch out and try each of those
- If any branch reaches a dead end, stop having that branch go.
- at the end, pick the one that meets the criteria (fewest, most, etc)

Where I struggle is how to do the second step. 

Looks like I'm finally learning BFS. 

I'm going to be adapting the code from https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/ to work with my grid. I don't normally bother with classes and I think namedTuple might even work better here, but for simplicity's sake I'm going to go with their method.
### Part 2
Just iterate and hope that it doesn't need a more efficient algorithm. 
## What I Learned

### Generic
I think I finally understand (for the first time since undergrad) how Breadth First Search works (and can probably turn around and use it for 2016).

Essentially, from the starting point, we look in all valid cardinal directions. If we find valid points to add, we put them in a queue.

The IMPORTANT thing is that we're using a deque, so we can lef-pop the list. This means that we're always checking every node at the same level (the same distance) and, therefore, will find the destination in the shortest distance possible.

Anyone else in the queue who could also reach the destination is at the same distance cost so whenever we get to the destination, we have found the shortest route.

Very awesome!!
### Python
- Generating BFS in Python
### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    