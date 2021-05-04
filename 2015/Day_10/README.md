# Day 10: Elves Look, Elves Say

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/10).

## Part 1

...playing a game called [look-and-say](https://adventofcode.com/2015/day/10). They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

- 1 becomes 11 (1 copy of digit 1).
- 11 becomes 21 (2 copies of digit 1).
- 21 becomes 1211 (one 2 followed by one 1).
- 1211 becomes 111221 (one 1, one 2, and two 1s).
- 111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 1321131112.

Answer: 492982

## Commentary
I originally wanted to tackle this with a regex. But that turned out not to work the way I wanted. Apparently there's a command
in Haskell that could have done this problem very easily. After a couple false starts, I arrived at a good method.

I'm pretty sure I was supposed to somehow make use of the algorithm on the Wikipedia page because this takes a good 45 seconds or so to run.

## Part 2

## What I Learned for Each Language

### Python
- Nothing

### Ruby
- Learned about chunk and how it's basically what I had read existed in Haskell (in Haskell it’s the group function). In Ruby chunk_while is actually a little more flexible than group (at least as presented in Learn You A Haskell for Great Good!) and can be used to group together sequential items in a list based on all kinds of boolean expressions. However, if with the a == b boolean, we get a list that keeps getting new items as long as they equal the previous one .After that it was a matter of putting the size of the list into the output to create the look-and-say pattern. Much easier than Python.
    
### Perl

- Using [Array::Groupby](https://metacpan.org/pod/Array::GroupBy) to achieve the same result as `chunk_while` in Ruby.