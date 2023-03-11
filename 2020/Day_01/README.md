# Day 1- Report Repair

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/1).

## Part 1

For part one you have a list of numbers, eg:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Find the two entries that sum to 2020; what do you get if you multiply them together? (that's what gets you a star for this problem)

Answer: 145875

## Part 2

Find three numbers in your list that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

What is the product of the three entries that sum to 2020?

Answer: 69596112

## Commentary / Approach to the Problem
Back when I originally solved this with Python in 2020 (during AoC), I had been reading a few different Python books that were highlighting various libraries like Collections and Itertools so I ended up solving this problem in a much more complicated way than you'll see around the net. 

I created pairs out of all the numbers in my inputs and then I checked to find the pair that summed to 2020. For part 2 I did the same thing with triples.

When I come back to this to solve it with other programming languages, I intend to take the easier, less complex approach.

That less complex approach is to take 2020, subtract one of the numbers. See if the answer is in list. Then you have your pair.

## What I Learned

### Generic

### Python
- Cemented knowledge of, and how to work with, Combinations from Itertools.

### Ruby

### Perl

### Go
- Nothing new