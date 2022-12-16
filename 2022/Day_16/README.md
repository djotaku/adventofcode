# Day 16 - Proboscidea Volcanium

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/16).

## Part 1

## Part 2

## Commentary / Approach to the Problem
### Part 1
- Create a namedTuple - valve with attributes of pressure and a list of tunnels
- First off, ingest the input and create a dictionary where the key is the valve and the value is the namedTuple
- I’m thinking a modified BFS (or something similar) where for each round you compute the value of the path you’ve chosen. (pressure being relieved * time left) and you pick the largest one. Or is it more like a graph traversal where the value of the line has to be calculated in that moment (vs at first?)
- And a friend mentioned that in the sample algorithm we're going back and forth to the same valve more than once. 
- Currently thinking a Traveling Salesman (or Hamiltonian walk or something) where you can visit the same place once and what prevents an infinite loop is running out of time. Might blow up RAM or CPU, though.

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
    