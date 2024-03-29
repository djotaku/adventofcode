# Day 01 - Inverse Captcha

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2017/day/1).

## Part 1
Answer: 1089

## Part 2
Answer: 1156

## Commentary / Approach to the Problem

### Part 1
Looks like I'll use the strategy I used for 2015 Day 05:

```python
double_letter = re.compile(r'(.)\1')
```

Then do a separate check to compare the first and last number.

### Part 2
I think for this part, it's probably better not to use regex. Just search within Python. 

## What I Learned

### Generic

### Python
- A new type of lookahead in order to allow for overlapping without using the regex module. re.compile(r'(\d)(?=\1)')

### Ruby
- A reminder that array.each_with_index is the equivalent to Python's enumerate(list)
### Perl

### Go (Golang)
- Go does not support lookaheads in regular expressions
- I continue to rue runes and how they are what you get from strings
### Haskell

### Rust

### Julia
    