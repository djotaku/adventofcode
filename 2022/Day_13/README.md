# Day 13 - Distress Signal

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/13).

## Part 1
Answer: 5843
## Part 2

## Commentary / Approach to the Problem
### Part 1
I think the hardest parts will be parsing the input and keeping the comparisons from getting messy. The actual comparisons shouldn't be too hard.

One exception that might make the comparisons tricky is the requirement to convert non-lists into lists. 

I'm torn about whether it's a better strategy to actually turn the inputs into lists or keep it text and parse out what's a list. I've done stuff like that in the past when 
we were asked to change the order of operations of math, but I can't say that code was necessarily very pretty to work with. 
Still, I may look back on that for inspiration. 

Looking at the input, there may be some shortcuts that can be taken. For example, count opening '[' and if they don't match, that might be a quick eval.
Also, just compare lengths and if they are off by a LOT, may be easy to just make a judgement.

Was having trouble getting my comparison recurion to work, so I modified things based on [this solution](https://www.reddit.com/r/adventofcode/comments/zkmyh4/comment/j098dd5/?utm_source=share&utm_medium=web2x&context=3) 

### Part 2
Basically write a sort method...
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    