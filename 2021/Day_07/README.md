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

Answer: 344297

## Part 2
crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

- Move from 16 to 5: 66 fuel
- Move from 1 to 5: 10 fuel
- Move from 2 to 5: 6 fuel
- Move from 0 to 5: 15 fuel
- Move from 4 to 5: 1 fuel
- Move from 2 to 5: 6 fuel
- Move from 7 to 5: 3 fuel
- Move from 1 to 5: 10 fuel
- Move from 2 to 5: 6 fuel
- Move from 14 to 5: 45 fuel

This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?

Answer: 

## Commentary / Approach to the Problem
### Part 1
Two approaches came to me at first. The naive approach - calculate the fuel for each position and sum the min fuel consumption.

The other approach, I can "vocalize", but have to think about programming it. Figure out where the highest distribution of crabs is and search around that space. The example input, for example, has mostly small numbers and 3 crabs already at position 2. I don't quite have the math training I'd need for that, but perhaps finding the average could point me in the right directions as a place to start. If it's like yesterday where part 2 is the same, but more, then this would definitely be the approach. 

I plan to start with the naive approach and go from there.

### Part 2
Looks like I can continue with the naive approach, but will want to factor this out to a function.

[A little googling brought me to the equation I needed.](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF) I literally just googled 1+2+3+4 series. That gave me the equation I needed. 

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
    