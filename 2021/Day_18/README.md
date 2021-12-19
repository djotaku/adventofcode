# Day 18: Snailfish

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/18).

## Part 1

## Part 2

## Commentary / Approach to the Problem
### Part 1
For some reason, this seems to me like it might be awesome for Haskell.

Anyway, it seems to me that the approach to take is to design a recursive function. If either explosion or splitting needs to happen, do it then call the function again. If none of them have to be done you're at the base case and you just return.

I got to about [here](https://github.com/djotaku/adventofcode/blob/461f12d2bc9b82fa506abe182bb5e9eee47163f1/2021/Day_18/Python/solution.py) before wondering if I could just make use of Python's lists to make the parsing easier? So I did a bit of Googling and it took some time to find, but you could do a json.loads to get the string into a list. So I decided to try that.

This was also a dead end.
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
