# Timing is Everything

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/15).

## Part 1
Furthermore, the discs are spaced out so that after you push the button, one second elapses before the first disc is reached, and one second elapses as the capsule passes from one disc to the one below it. So, if you push the button at time=100, then the capsule reaches the top disc at time=101, the second disc at time=102, the third disc at time=103, and so on.

The button will only drop a capsule at an integer time - no fractional seconds allowed.

For example, at time=0, suppose you see the following arrangement:

- Disc #1 has 5 positions; at time=0, it is at position 4.
- Disc #2 has 2 positions; at time=0, it is at position 1.
If you press the button exactly at time=0, the capsule would start to fall; it would reach the first disc at time=1. Since the first disc was at position 4 at time=0, by time=1 it has ticked one position forward. As a five-position disc, the next position is 0, and the capsule falls through the slot.

Then, at time=2, the capsule reaches the second disc. The second disc has ticked forward two positions at this point: it started at position 1, then continued to position 0, and finally ended up at position 1 again. Because there's only a slot at position 0, the capsule bounces away.

If, however, you wait until time=5 to push the button, then when the capsule reaches each disc, the first disc will have ticked forward 5+1 = 6 times (to position 0), and the second disc will have ticked forward 5+2 = 7 times (also to position 0). In this case, the capsule would fall through the discs and come out of the machine.

What is the first time you can press the button to get a capsule?

Answer: 203660
## Part 2
a new disc with 11 positions and starting at position 0 has appeared exactly one second below the previously-bottom disc.

With this new disc, and counting again starting from time=0 with the configuration in your puzzle input, what is the first time you can press the button to get another capsule?

Answer: 2408135

## Commentary / Approach to the Problem
### Part 1
This seems similar to the bus problem from 2020. I need to figure out the math that would allow this to shortcut instead of running a
simulation. I think that a sim might work OK for part 1, but I'm pretty sure it won't work for part 2.

First guess is that I add 1 to the modulo per each disc to allow for the second that each disc consumes.

Eventually, I ended up going with the direct simulation route.

### Part 2
First attempt will be to simply insert the new disc into the list and see if that works.

## What I Learned

### Generic

### Python
- Nothing
### Ruby

### Perl

### Go (Golang)

### Haskell
