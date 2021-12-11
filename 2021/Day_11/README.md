# Day 11: Dumbo Octopus

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/11).

## Part 1
There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains energy over time and flashes brightly for a moment when its energy is full.

Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus (your puzzle input). For example:

    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526

The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5, the bottom-right one has an energy level of 6, and so on.

You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

- First, the energy level of each octopus increases by 1.
- Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
- Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.

Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. How many total flashes are there after 100 steps?

Answer: 1747

## Part 2
the flashes seem to be synchronizing!

In the example above, the first time all octopuses flash simultaneously is step 195:

 What is the first step during which all octopuses flash?

Answer: 505

## Commentary / Approach to the Problem
### Part 1
While I don't think this is the Conway for this year, it's one of those problems where neighbors affect each other. 

As I've learned, this is best done with a dictionary in Python. 

I'm not sure yet how to deal with the octopuses only flashing once per step. One possibility is to make each octopus an object (or named tuple? Have to see if those values can change since it's a tuple. (after a google search) Nope - can't change) that stores both level and whether it has flashed this step. Or just have it be a list where the second element is whether it has flashed this step. Went with class objects, inspired by the Kotlin blog solutions this year.

Overall it wasn't too hard, although a typo on line 37 led to wasted time debugging. Creating the octopus class helped make it more readable, but did make debugging a bit harder.

### Part 2
Just had to add a couple checks to my loops to catch the number of flashes at 100 and stop when 100 of them had flashed. It was off by 1 although I'm not 100% sure why. Although off-by-one is the classic CS error.

## What I Learned

### Generic

### Python
- Nothing
### Ruby
- TBD
### Perl
- TBD
### Go (Golang)
- TBD
### Haskell
- TBD