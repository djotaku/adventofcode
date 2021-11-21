# Day 5: How About a Nice Game of Chess?

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/5). 

## Part 1
The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password.

For example, if the Door ID is abc:

- The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
- 5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the password is 8.
- The third time a hash starts with five zeroes is for abc5278568, discovering the character f.
In this example, after continuing this search a total of eight times, the password is 18f47a30.

Given the actual Door ID, what is the password?

Your puzzle input is ugkcyxxp.

Answer: d4cd2ee1

## Part 2

## Commentary / Approach to the Problem
### Part 1
In 2015 Day 4 I used the hashing algorithms for Python, Perl, and Ruby. So I decided to start there. Part 1 seemed pretty easy and straightforward. I was able to take that 2015 code and just modify it slightly to get the answer to part 1.

### Part 2
Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position.

A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

- The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
- In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an invalid position (8).
- The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.

producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password?

Answer: f2c730e5
## What I Learned

### Generic

### Python
- Nothing new
### Ruby

### Perl
- Very easy, just required remembering substr function.
- using defined keyword to check if a variable is undefined.
### Go (Golang)

### Haskell
