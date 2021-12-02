# Day 1: Sonar Sweep

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/1).

## Part 1
...[your puzzle input] appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

    199
    200
    208
    210
    200
    207
    240
    269
    260
    263

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases

count the number of times a depth measurement increases from the previous measurement

In the example above, the changes are as follows:

    199 (N/A - no previous measurement)
    200 (increased)
    208 (increased)
    210 (increased)
    200 (decreased)
    207 (increased)
    240 (increased)
    269 (increased)
    260 (decreased)
    263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

Answer: 1602

## Part 2
consider sums of a three-measurement sliding window. Again considering the above example:

    199  A      
    200  A B    
    208  A B C  
    210    B C D
    200  E   C D
    207  E F   D
    240  E F G  
    269    F G H
    260      G H
    263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases

Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

    A: 607 (N/A - no previous sum)
    B: 618 (increased)
    C: 618 (no change)
    D: 617 (decreased)
    E: 647 (increased)
    F: 716 (increased)
    G: 769 (increased)
    H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

Answer: 1633

## Commentary / Approach to the Problem
Since I was very excited that it was the first day of Advent of Code, I tried to get it done before heading out to work so I just did the first solution that came to mind. A couple of simple for loops handled things for me. 

## What I Learned

### Generic
With my own solutions I didn't learn anything, but going into the Day 01 Megathread I learned a couple awesome things. First of all, the best and most elegant Python solution I saw was:

```python
part1 = sum((b>a) for (a,b) in zip(input,input[1:]))
part2 = sum((b>a) for (a,b) in zip(input,input[3:]))
```

The more impressive thing was the person who pointed out:

    x + y + z < y + z + a
    is the same as
    x < a

That just blew my mind! How do people just look at the problem and have that pop out at them?

### Python
- Nothing today
### Ruby

### Perl

### Go (Golang)
- Nothing new learned for go, but I did use the  x + y + z < y + z + a principle to simplify my part 2 answer compared to Python
### Haskell
    