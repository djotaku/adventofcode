# Day 23 - Crab Cups

[Story Text](https://adventofcode.com/2020/day/23)

## Part 1

The cups will be arranged in a circle and labeled clockwise (your puzzle input). 
For example, if your labeling were 32415, there would be five cups in the circle; 
going clockwise around the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5, and then back to 3 again.

Before the player starts, it will designate the first cup in your list as the current cup. The player is then going to do 100 moves.

Each move, the player does the following actions:

- The player picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
- The player selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
- The player places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
- The player selects a new current cup: the cup which is immediately clockwise of the current cup.

Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?

## Part 2

TBD