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

Answer: 535

## Part 2

Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time, just like the ones during calibration.

For example, suppose you have the following replacements:

- e => H
- e => O
- H => HO
- H => OH
- O => HH

If you'd like to make HOH, you start with e, and then make the following replacements:

- e => O to get O
- O => HH to get HH
- H => OH (on the second H) to get HOH

So, you could make HOH after 3 steps. Santa's favorite molecule, HOHOHO, can be made in 6 steps.

How long will it take to make the medicine? Given the available replacements and the medicine molecule in your puzzle input, what is the fewest number of steps to go from e to the medicine molecule?

Answer: 
## Commentary / Approach to the Problem
Part 1 wasn't too hard to figure out. It mostly involved checking the Python libraries to see how to get the positions in the string for the matches. But on the first day that I read part 2, I had no idea whatsoever how to begin.

## What I Learned

### Generic

### Python
- The existence of re.finditer to find out where in a string your match occurred.

### Ruby
- getting better at using map (in this case map!) to do the equivalent of Python's list comprehensions. It took me a while, but I'm particularly proud of how the generate_molecule_tuple turned out.
- using str.to_enum(:scan, regular expression).map { Regexp.last_match} to do the equivalent of Python's re.finditer
### Perl

