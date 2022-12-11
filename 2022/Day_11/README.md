# Day 11 - Monkey in the Middle

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/11).

## Part 1
Answer: 58786
## Part 2
Answer: 14952185856
## Commentary / Approach to the Problem
### Part 1
Because we have to keep track of how many times a monkey has inspected an item, I will have a dictionary of monkeys. One key will be items and it will hold a deque of items so I can do a pop from the left. Another key will hold a count of inspected items. 
Other keys will hold their operation and test values.

### Part 2
So I quickly realized that the problem is that our worry value was getting too high. Initially I considered not squaring the item number for the monkey that did that as a number and that number squared have the same modulo. But that wasn't right.  I looked around online and I was in the right ballpark, even if I wasn't doing it right.
This [subreddit answer](https://www.reddit.com/r/adventofcode/comments/zih7gf/comment/izr79go/?utm_source=share&utm_medium=web2x&context=3) is what I did to get the right answer.
## What I Learned

### Generic
- A little more about math, modulo, and keeping numbers sane.
### Python

### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    