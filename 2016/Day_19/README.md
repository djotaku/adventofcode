# An Elephant Named Joseph 

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/19).

## Part 1
Each Elf brings a present. They all sit in a circle, numbered starting with position 1. Then, starting with the first Elf, they take turns stealing all the presents from the Elf to their left. An Elf with no presents is removed from the circle and does not take turns.

For example, with five Elves (numbered 1 to 5):

- Elf 1 takes Elf 2's present.
- Elf 2 has no presents and is skipped.
- Elf 3 takes Elf 4's present.
- Elf 4 has no presents and is also skipped.
- Elf 5 takes Elf 1's two presents.
- Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
- Elf 3 takes Elf 5's three presents.
So, with five Elves, the Elf that sits starting in position 3 gets all the presents.

With the number of Elves given in your puzzle input, which Elf gets all the presents?

Your puzzle input is 3018458.

Answer: 1842613
## Part 2
Unsure how to setup the circles.

## Commentary / Approach to the Problem
### Part 1
Since we don't care about the number of presents, just who ends up with all of them, I set up a dictionary with True for each elf. Then I loop through and have them steal from each other (make that elf's value False)
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
