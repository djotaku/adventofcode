# Day 4: Giant Squid

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/4).

## Part 1

## Part 2

## Commentary / Approach to the Problem
### Part 1
OK, so it looks like we need to program a bingo simulator. We have a few things I think I need to do (based on the way my brain works)

- Take care of the input to parse out boards and the bingo numbers that will be called
- Figure out how to represent the boards. Initial thought is to have a dictionary of dictionaries in which the inner dictionaries have keys being the (x,y) coords of the board. Then the value is a list where item 0 is the number and item 1 is whether that number wins
- Then I do a check after each number is called to see if a row wins
- Then calculate the score

I'm guessing there may be a simpler way where I don't need to keep track of whether a number has been called. Instead I can check all numbers that have been called so far against all rows and columns (I'm going to guess that part 2 is going to also consider diagonals). But it may be simpler logic to just do a check for what's already matched. Time will tell as I get into it. 

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
    