# Day 19: Medicine for Rudolph

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/19).

## Part 1
 It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

- H => HO
- H => OH
- O => HH

Given the replacements above and starting with HOH, the following molecules could be generated:

- HOOH (via H => HO on the first H).
- HOHO (via H => HO on the second H).
- OHOH (via H => OH on the first H).
- HOOH (via H => OH on the second H).
- HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?
## Part 2

## Commentary / Approach to the Problem

## What I Learned

### Generic

### Python

### Ruby

### Perl

