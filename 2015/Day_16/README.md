# Day 16: Aunt Sue

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/16).

## Part 1
You need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! 

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

- children, by human DNA age analysis.
- cats. It doesn't differentiate individual breeds.
- Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
- goldfish. No other kinds of fish.
- trees, all in one group.
- cars, presumably by exhaust or gasoline or something.
- perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

- children: 3
- cats: 7
- samoyeds: 2
- pomeranians: 3
- akitas: 0
- vizslas: 0
- goldfish: 5
- trees: 3
- cars: 2
- perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

Answer: 
Aunt Sue 40

## Part 2

The output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

Answer: 241
## Commentary / Approach to the Problem

I'm pretty sure I didn't do the most efficient algorithm. Looking back on it, I think I should have created a function that returned whether or not a particular key should be deleted. (At least for Python and Ruby) 

## What I Learned

### Generic

### Python
- On lines where I was doing the less than comparison it was failing if it was a None value. So I had to make use of the fact order in which truthiness is evaluated in Python to make the order go away. I had to check for None and THEN check numerically.
### Ruby
- Although I'm sure I did this in a horribly inefficient way (the fact that I'm repeating over and over would seem to indicate this), I learned about Hash#keep_if - very neat!
### Perl
- Mostly applied the lessons I learned for part 2 in Python and Ruby to get the right order for checking things. In Perl I had to do this in part 1 and check for existence of the key before testing the value of the key.

