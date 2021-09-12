# Day 2: Password Philosophy

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/2).

## Part 1

Suppose you have the following list:

- 1-3 a: abcde
- 1-3 b: cdefg
- 2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Answer: 586

## Part 2

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

Answer: 352

## Commentary / Approach to the Problem
When I first worked on this problem in Python in 2020 (during AoC), I merely used Python built-ins for part 1. I used split to create lists with the policy, min, and max. It worked just fine and the input wasn't too computationally complex. I think if I were working the problem in 2021, I'd use a regex to grab the values and have a less complex set of lists.

I think most of what I did for part 2 with Python makes sense but might have been easier to follow if I'd started with a simpler part 1.

## What I Learned

### Generic

### Python
- Nothing

### Ruby

### Perl

