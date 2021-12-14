# Day 14: Extended Polymerization

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/14).

## Part 1
You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

    NNCB
    
    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C

The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

- The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
- The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
- The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.

Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

aking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

Answer: 3906

## Part 2
Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

Answer: 
## Commentary / Approach to the Problem
### Part 1
Originally I was intending to use regexes and do part 1 manually and hope that part 2 wasn't a redo of 2015's [Day 19: Medicine for Rudolph.](https://github.com/djotaku/adventofcode/tree/b01d90108d87c0a55dfd781f3b5558bcd1b714ba/2015/Day_19). But in discussing part 2 with a colleague (I usually try to avoid discussing spoilers, but it happens), he mentioned the best strategy is to treat it like this year's [lanternfish problem](https://github.com/djotaku/adventofcode/tree/b01d90108d87c0a55dfd781f3b5558bcd1b714ba/2021/Day_06).

So what was left was to figure out how I wanted to parse the pairs since the second letter in each pair is the first letter of the next pair. I could try some sort of recursive regex or just a for loop. I decided to go with a for loop.

I am not sure the person who said it was like the lanternfish actually tried to solve the problem. Wasn't able to do what he described. So I did it a completely different way.

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
