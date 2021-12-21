# Day 15: Chiton

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/15).

## Part 1
 The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

    1163751742
    1381373672
    2136511328
    3694931569
    7463417111
    1319128137
    1359912421
    3125421639
    1293138521
    2311944581

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

    *1*163751742
    *1*381373672
    *2**1**3**6**5**1**1*328
    369493*1**5*69
    7463417*1*11
    1319128*1**3*7
    13599124*2*1
    31254216*3*9
    12931385*2**1*
    231194458*1*

The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1
I was at first thinking of maybe using a Hamilton Path or Traveling Salesman, but I think (at least the way I was thinking about it) it wouldn't work well. So instead I decided to try and go with the same algorithm as for the caves. I would link each node to its cardinal direction neighbors and then capture the numbers to sum at the end. 

The cave algorithm - BFS - was the wrong algorithm to use. It was more or less infinite.

Someone told me to use Dijkstra. I'd tried last year and earlier this year, but I guess it was time to finally learn it. [I'm using a stack abuse page](https://stackabuse.com/dijkstras-algorithm-in-python/) to learn Dijkstra/use their implementation, but I'll still have to format the input to work with it.
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
