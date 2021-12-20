# Day 18: Snailfish

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/18).

## Part 1
This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

    If any pair is nested inside four pairs, the leftmost such pair explodes.
    If any regular number is 10 or greater, the leftmost such regular number splits.

Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?

To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of [9,1] is 3*9 + 2*1 = 29; the magnitude of [1,9] is 3*1 + 2*9 = 21. Magnitude calculations are recursive: the magnitude of [[9,1],[1,9]] is 3*29 + 2*21 = 129.

Answer: 3051
## Part 2
What is the largest magnitude you can get from adding only two of the snailfish numbers?

What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?

Answer: 4812

## Commentary / Approach to the Problem
### Part 1
For some reason, this seems to me like it might be awesome for Haskell.

Anyway, it seems to me that the approach to take is to design a recursive function. If either explosion or splitting needs to happen, do it then call the function again. If none of them have to be done you're at the base case and you just return.

I got to about [here](https://github.com/djotaku/adventofcode/blob/461f12d2bc9b82fa506abe182bb5e9eee47163f1/2021/Day_18/Python/solution.py) before wondering if I could just make use of Python's lists to make the parsing easier? So I did a bit of Googling and it took some time to find, but you could do a json.loads to get the string into a list. So I decided to try that.

[This was also a dead end](https://github.com/djotaku/adventofcode/blob/586294696f71f49877434bce1e77c1cd9257d0e7/2021/Day_18/Python/solution_with_json.py).

I decided to do what I've been doing so far this year - check the megathread and see if I could reason out a solution based on what others had done. Most people were doing stuff with trees. I did find [one solution](https://github.com/Gravitar64/Advent-of-Code-2021/blob/82f7e8aa1d91c87149af059af9a69545ba48708f/Tag_18.py) that I thought I might want to adapt. This person records the depths as part of a tuple with the number. This helps with the situation I was coming up against in my first solution where I might need to backtrack or go forward to figure out the numbers for addition.

I was able to make a few improvements, including making the magnitude calculation truly recursive and using math.floor and math.ciel. I also realized I need to get a better intuition for when to use zip.

## What I Learned

### Generic

### Python
- use of continue in a for loop to return to the beginning of the for loop
- need to get better at when to use zip
### Ruby
- TBD
### Perl
- TBD
### Go (Golang)
- TBD
### Haskell
- TBD