# Day 20 - Grove Positioning System

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/20).

## Part 1

## Part 2

## Commentary / Approach to the Problem
### Part 1
This seems deceptively simple for part one. I mean, it's rife with possibilities for bugs in the wrapping code or placement after the mixing, but it doesn't seem hard conceptually.

Since they are moved in the original order of the list (and because Python, at least, does not support changing a list as you iterate), I think perhaps it's best to grab a number and its position, then record where it should go. At the end, put all the numbers into a new list. 

I'll try this with the sample first, and see what happens.

This doesn't work because, while the numbers have to go in order, they have to deal with the mutated list. I have an idea, but it will only work if the real input contains no duplicates. 

I use the original list to search for numbers and modify where they are in the list. However, I think that will probably quickly overwhelm my computer - especially in part 2. I'm not currently seeing how to do it with a dict/map/hash. Probably a linked list? 
(Not that I remember how to do that) 

Turns out numbers aren't unique. So I may have to do this in a more brute force manner.

Tried to make my code more like this guy's: https://www.reddit.com/r/adventofcode/comments/zqezkn/comment/j11n0z3/?utm_source=share&utm_medium=web2x&context=3 but still kept getting the wrong answer. Perhaps because I wasn't making the number class? Therefor the duplicate numbers were still causing me issues? 
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
    