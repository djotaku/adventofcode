# Day 7: Internet Protocol Version 7

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/7).

## Part 1
An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

- abba[mnop]qrst supports TLS (abba outside square brackets).
- abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
- aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
- ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1
Once again, 2015 Day 5 might help because it showed how to look for letters in certain patterns. Idea is to evaluate each line against the 3 rules we know, eliminating any that don’t pass all three rules.
- ABBA
- A and B are different
- ABBA not found in brackets

## What I Learned

### Generic
- used the awesome regex101.com to figure out the regex expressions for the rules
### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
