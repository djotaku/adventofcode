# Day 4: The Ideal Stocking Stuffer

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/4).

## Part 1

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. You must the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

- If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
- If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

Answer: 346386

## Part 2

TBD

## Commentary

These are my least favorite puzzles because if I can't figure out how to do a MD5 hash or my programming language doesn't have a library for it, then I'm stuck on that rather than trying to solve the problem. That said, I have no idea what strategy I would use other than brute force. 


## What I Learned

### Python

### Ruby

### Perl