# Day 21 - Monkey Math

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/21).

## Part 1
Answer: 31017034894002
## Part 2

## Commentary / Approach to the Problem
### Part 1
This reminds me a lot of the problem from [2015 Day 7](https://github.com/djotaku/adventofcode/blob/main/2015/Day_07/Python/part_1_memoization.py) so I'm going to start off with that as my solution idea.

That is, use an lru cache and a dictionary to recursively find the answer for the root monkey's math.

This turned out to be perfect and the result was immediately returns.

### Part 2

I *think* this should be doable without TOO much trouble. Just modify the dictionary value of root and humn and run things (maybe with a slightly different function.) More or less runs forever. 

Will need to come up with a different approach for part 2. Some folks did the equations backwards to solve for humn. There may be other ways to do it. 

## What I Learned

### Generic

### Python
- You need to clear the lru_cache if you're going to use it more than once!
### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
