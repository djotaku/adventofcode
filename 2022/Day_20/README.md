# Day 20 - Grove Positioning System

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/20).

## Part 1
Answer: 13183
## Part 2
Answer: 6676132372578
## Commentary / Approach to the Problem
### Part 1
This seems deceptively simple for part one. I mean, it's rife with possibilities for bugs in the wrapping code or placement after the mixing, but it doesn't seem hard conceptually.

Since they are moved in the original order of the list (and because Python, at least, does not support changing a list as you iterate), I think perhaps it's best to grab a number and its position, then record where it should go. At the end, put all the numbers into a new list. 

I'll try this with the sample first, and see what happens.

This doesn't work because, while the numbers have to go in order, they have to deal with the mutated list. I have an idea, but it will only work if the real input contains no duplicates. 

I use the original list to search for numbers and modify where they are in the list. However, I think that will probably quickly overwhelm my computer - especially in part 2. I'm not currently seeing how to do it with a dict/map/hash. Probably a linked list? 
(Not that I remember how to do that) 

Turns out numbers aren't unique. So I may have to do this in a more brute force manner.

Tried to make my code more like this guy's: https://www.reddit.com/r/adventofcode/comments/zqezkn/comment/j11n0z3/?utm_source=share&utm_medium=web2x&context=3 but still kept getting the wrong answer. Perhaps because I wasn't making the number class? Therefor the duplicate numbers were still causing me issues? The key turned out to be his use of a Number class which made
it so that the list items weren't duplicates anymore.

Another thing I might consider for other language implementations is to have a dictionary with the numbers as the key and I can add a suffix when a number 
appears more than once. And I could move keys around and then look up the values at the end.
### Part 2

OK, things are about to get hairy. Especially because I'm not 100% sure (based on Wastl's use of -3) exactly when I'm multiplying. But I'll give it a shot!

The only tricky thing was making sure to generate the part 2 list before moving stuff around so you get the initial placement.
## What I Learned

### Generic

### Python
- A default empty list has no positions, making it hard to put new numbers in there. Need to create a list with 0s or something first.
- a trick to search a list that has duplicates is to use a class because each class will have a unique "id"
### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    