# Day 04 - Camp Cleanup

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/4).

## Part 1
To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:
```
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
```
For the first few pairs, this list means:

- Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
- The Elves in the second pair were each assigned two sections.
- The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

In how many assignment pairs does one range fully contain the other?

Answer: 528

## Part 2
In how many assignment pairs do the ranges overlap? (to any degree)

Answer: 881

## Commentary / Approach to the Problem
### Part 1

- Create sets with all items in the range
- Use issubset method (you probably need to do it on each one to make sure in case he gives it in an order where sometimes the left is subset and sometimes right is subset

### Part 2

Use isdisjoint to see if there's any overlap.
 
## What I Learned

### Generic

### Python
- set.issubset
- set.isdisjoint
### Ruby
- subset?
- disjoint?

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    