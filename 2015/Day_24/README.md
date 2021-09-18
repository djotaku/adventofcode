# Day 24: It Hangs in the Balance

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/24).

## Part 1
Santa has provided you a list of the weights of every package he needs to fit on the sleigh. The packages need to be split into three groups of exactly the same weight, and every package has to fit. The first group goes in the passenger compartment of the sleigh, and the second and third go in containers on either side. Only when all three groups weigh exactly the same amount will the sleigh be able to fly. Defying physics has rules, you know!

Of course, that's not the only problem. The first group - the one going in the passenger compartment - needs as few packages as possible so that Santa has some legroom left over. It doesn't matter how many packages are in either of the other two groups, so long as all of the groups weigh the same.

Furthermore, Santa tells you, if there are multiple ways to arrange the packages such that the fewest possible are in the first group, you need to choose the way where the first group has the smallest quantum entanglement to reduce the chance of any "complications". The quantum entanglement of a group of packages is the product of their weights, that is, the value you get when you multiply their weights together. Only consider quantum entanglement if the first group has the fewest possible number of packages in it and all groups weigh the same amount.

What is the quantum entanglement of the first group of packages in the ideal configuration?

Answer: 11846773891

## Part 2

## Commentary / Approach to the Problem
Seems like a more elaborate version of [Day 17](https://adventofcode.com/2015/day/17) 
- First need to sum weights and divide by 3. That tells you the weight that has to be in each group.
- I wonder if you can ignore groups 2 and 3 for part one? Just do combos/permutations and pick the one that has the smallest number of members and/or quantum entanglement if necessary

## What I Learned

### Generic

### Python

### Ruby

### Perl

