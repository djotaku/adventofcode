# Day 23 - Safe Cracking

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/23).

## Part 1
Answer: 11500
## Part 2

Answer: 479008060

## Commentary / Approach to the Problem
### Part 1
Initial idea is to create a function that will figure out what to change with tgl. Might do if/else or match statements.
Need to check not only the length of the list (how many arguments), but also if the toggled instruction is invalid.

### Part 2
I am guessing I need to change something to multiplication or the program runs forever? He mentions "add one", so I figure I can change that to multiply?

But the question is what do I multiply it by? Itself? 

I still couldn't figure it out, especially since my code didn't "overheat" for a=12. It actually finished just fine. Maybe there wsa just a bug in my code? (Which gave me the right answer for part 1?) Hopefully this doesn't make trouble for me for Day 25. 

Still it turns out the multiplication and bunnies was supposed to clue me in to factorial since that's something that's always used as an example with factorial. And there's a constant you get from the end of your input, mine is 

```
cpy 85 c
jnz 76 d
```
and you multiply those constants. Every year there's at least one problem like this where I have NO idea how to intuit from the clues provided. (The room where the ornaments are kept was another one that stumped me.)
## What I Learned

### Generic

### Python
- Nothing
### Ruby

### Perl

### Go (Golang)

### Haskell
