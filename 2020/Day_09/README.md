# Day 9: Encoding Error

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/9).

## Part 1

Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is 127.

find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?

Answer: 23278925

## Part 2

find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

Add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

Answer: 4011064

## Commentary / Approach to the Problem

## What I Learned
By using a deque with a maxlength, I reduce the complexity of finding the previous 5 numbers to sum. 
### Generic

### Python

### Ruby

### Perl

