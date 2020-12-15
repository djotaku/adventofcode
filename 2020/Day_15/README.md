[Cute Version](https://adventofcode.com/2020/day/15)

# Part 1

In this game, the players take turns saying numbers. They begin by taking turns reading from a list of starting numbers (your puzzle input). Then, each turn consists of considering the most recently spoken number:

- If that was the first time the number has been spoken, the current player says 0.
- Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.

So, after the starting numbers, each turn results in that player speaking aloud either 0 (if the last number is new) or an age (if the last number is a repeat).

hat will be the 2020th number spoken? In the example above, the 2020th number spoken will be 436.

Here are a few more examples:

- Given the starting numbers 1,3,2, the 2020th number spoken is 1.
- Given the starting numbers 2,1,3, the 2020th number spoken is 10.
- Given the starting numbers 1,2,3, the 2020th number spoken is 27.
- Given the starting numbers 2,3,1, the 2020th number spoken is 78.
- Given the starting numbers 3,2,1, the 2020th number spoken is 438.
- Given the starting numbers 3,1,2, the 2020th number spoken is 1836.

# Part 2