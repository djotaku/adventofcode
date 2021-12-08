# Day 7: The Treachery of Whales

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/7).

## Part 1
consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14

This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

- Move from 16 to 2: 14 fuel
- Move from 1 to 2: 1 fuel
- Move from 2 to 2: 0 fuel
- Move from 0 to 2: 2 fuel
- Move from 4 to 2: 2 fuel
- Move from 2 to 2: 0 fuel
- Move from 7 to 2: 5 fuel
- Move from 1 to 2: 1 fuel
- Move from 2 to 2: 0 fuel
- Move from 14 to 2: 12 fuel

This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

Answer:

## Part 2

## Commentary / Approach to the Problem
### Part 1
Two approaches came to me at first. The naive approach - calculate the fuel for each position and sum the min fuel consumption.

The other approach, I can "vocalize", but have to think about programming it. Figure out where the highest distribution of crabs is and search around that space. The example input, for example, has mostly small numbers and 3 crabs already at position 2. I don't quite have the math training I'd need for that, but perhaps finding the average could point me in the right directions as a place to start. If it's like yesterday where part 2 is the same, but more, then this would definitely be the approach. 

I plan to start with the naive approach and go from there.

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
    