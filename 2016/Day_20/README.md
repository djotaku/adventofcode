# Firewall Rules

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/20).

## Part 1
You've retrieved the list of blocked IPs from the firewall... rather than being written in dot-decimal notation, they are written as plain 32-bit integers, which can have any value from 0 through 4294967295, inclusive.

For example, suppose only the values 0 through 9 were valid, and that you retrieved the following blacklist:

- 5-8
- 0-2
- 4-7
The blacklist specifies ranges of IPs (inclusive of both the start and end value) that are not allowed. Then, the only IPs that this firewall allows are 3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle input), what is the lowest-valued IP that is not blocked?

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1
Potential strategy:
- A method that turns a range into a list of numbers (inclusive)
- Add those numbers into a set that contains invalid numbers
- Another set of all possible numbers
- Subtract the sets so you are left with a set of all valid numbers
- Put valid number set into a list and order numerically
- Smallest number is the answer

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
