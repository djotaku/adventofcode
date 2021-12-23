# Day 22: Reactor Reboot

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/22).

## Part 1
The reactor core is made up of a large 3-dimensional grid made up entirely of cubes, one cube per integer 3-dimensional coordinate (x,y,z). Each cube can be either on or off; at the start of the reboot process, they are all off

To reboot the reactor, you just need to set all of the cubes to either on or off by following a list of reboot steps (your puzzle input). Each step specifies a cuboid (the set of all cubes that have coordinates which fall within ranges for x, y, and z) and whether to turn all of the cubes in that cuboid on or off.

For example, given these reboot steps:

- on x=10..12,y=10..12,z=10..12
- on x=11..13,y=11..13,z=11..13
- off x=9..11,y=9..11,z=9..11
- on x=10..10,y=10..10,z=10..10

 y, and z) and whether to turn all of the cubes in that cuboid on or off.

For example, given these reboot steps:

on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
The first step (on x=10..12,y=10..12,z=10..12) turns on a 3x3x3 cuboid consisting of 27 cubes:

- 10,10,10
- 10,10,11
- 10,10,12
- 10,11,10
- 10,11,11
- 10,11,12
- 10,12,10
- 10,12,11
- 10,12,12
- 11,10,10
- 11,10,11
- 11,10,12
- 11,11,10
- 11,11,11
- 11,11,12
- 11,12,10
- 11,12,11
- 11,12,12
- 12,10,10
- 12,10,11
- 12,10,12
- 12,11,10
- 12,11,11
- 12,11,12
- 12,12,10
- 12,12,11
- 12,12,12

The initialization procedure only uses cubes that have x, y, and z positions of at least -50 and at most 50. For now, ignore cubes outside this region

Execute the reboot steps. Afterward, considering only cubes in the region x=-50..50,y=-50..50,z=-50..50, how many cubes are on?

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1
Building on what I learned doing the 2015 problem set for Conway stuff, I'm going to use dictionaries to implement this. 

Part 1 doesn't seem too bad. 

Steps:
- parse the inputs so I know my x, y, and z mins and maxes and if I'm turning off or on. Storing in a named tuple might make it easier to see what's going on.
- a function that takes in one line and either sets the coordinates to 0 or 1 and returns the dictionary to be used in the next calculate
- a function (using dictionary_name.get()) to get all the values from the -50-50 cuboid and sum it
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
