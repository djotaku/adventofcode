# Day 12: Passage Pathing

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/12).

## Part 1


## Part 2

## Commentary / Approach to the Problem
### Part 1
At first I was happy because I thought it was going to be a traveling salesman problem. I created an algorithm for that with the 2015 problem set. But this is different as we're allowed to revisit some locations and not others.

Before trying to take the input and massage it into a graph, I wanted to see if I could start with a graph and use that to get to the same solution as the problem. This would allow me to see if the graph method would work before spending too much time with parsing.

Thinking through my algorithm:
- How do we know when to end? When have we exhausted all possibilities?
- Obviously we want a set to store possibilities to negate duplicates
- Need to be able to throw away paths that cannot finish because they'd require going through a lowercase twice
- Do we need a tree or other recursive way of exploring every possible intersection? Or do we relay on randomness and enough turns to get it right? If so, do we split into multiple functions?

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
