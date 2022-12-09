# Day 08 -  Treetop Tree House

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/8).

## Part 1
you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

```
30373
25512
65332
33549
35390
```

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

- The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
- The top-middle 5 is visible from the top and right.
- The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
- The left-middle 5 is visible, but only from the right.
- The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
- The right-middle 3 is visible from the right.
- In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?

Answer: 1859
## Part 2
To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

consider the tree of height 5 in the middle of the fourth row:

```
30373
25512
65332
33549
35390
```

- Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
- Looking left, its view is not blocked; it can see 2 trees.
- Looking down, its view is also not blocked; it can see 1 tree.
- Looking right, its view is blocked at 2 trees (by a massive tree of height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?

Answer: 332640
## Commentary / Approach to the Problem
### Part 1
First pass at how to do this is to load the tree map into a dictionary. Then for each point on the map, see it can be seen in the cardinal directions.
### Part 2
Strategy here will be to utilize a similar algorithm as before, but this time I don't want true/false. I want to count until I get to a tree that's bigger or same size.
## What I Learned

### Generic

### Python
- A reminder that reversed(range()) reverses a range
### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    