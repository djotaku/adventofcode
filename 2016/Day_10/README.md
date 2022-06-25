# Day 10: Balance Bots

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/10).

## Part 1
Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

- value 5 goes to bot 2
- bot 2 gives low to bot 1 and high to bot 0
- value 3 goes to bot 1
- bot 1 gives low to output 1 and high to bot 0
- bot 0 gives low to output 2 and high to output 0
- value 2 goes to bot 2

Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

## Part 2

## Commentary / Approach to the Problem
### Part 1
As I initially think about this, I cannot think of the "smart" way to do this. So for now I'm thinking of a loop that goes over a list of robot objects. Each robot is asked if it has 2 values. If it does, it checks if comparing 61 to 17. If so, stop. We know the robot. Otherwise, pass on the numbers. 

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
