# Day 5: How About a Nice Game of Chess?

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/5). 

## Part 1
The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is abc:

The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
The third time a hash starts with five zeroes is for abc5278568, discovering the character f.
In this example, after continuing this search a total of eight times, the password is 18f47a30.

Given the actual Door ID, what is the password?

Your puzzle input is ugkcyxxp.

Answer: d4cd2ee1

## Part 2

## Commentary / Approach to the Problem
### Part 1
In 2015 Day 4 I used the hashing algorithms for Python, Perl, and Ruby. So I decided to start there. Part 1 seemed pretty easy and straightforward. I was able to take that 2015 code and just modify it slightly to get the answer to part 1.

### Part 2


## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
