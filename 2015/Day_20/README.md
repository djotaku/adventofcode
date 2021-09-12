# Day 20: Infinite Elves and Infinite Houses

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/20).

## Part 1
Santa has [Elves] deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

- The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
- The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
- Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

    House 1 got 10 presents.
    House 2 got 30 presents.
    House 3 got 40 presents.
    House 4 got 70 presents.
    House 5 got 60 presents.
    House 6 got 120 presents.
    House 7 got 80 presents.
    House 8 got 150 presents.
    House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle input is 34000000.

Answer: 

## Part 2

## Commentary / Approach to the Problem
Started off with the guess that: For any house the formula is -> Sum(F1*10+F2*10…..FN*10) where F is a factor of the number.  I think this means you can factor out the 10 and divide 10 from the number they give us. 

Did some non-AoC research (that is to say, I didn't look at anyone's solutions) and I think that meant I needed to compute the sum of divisors. [Here](https://mathschallenge.net/library/number/sum_of_divisors) is a site that explains that. Basically I need to find the prime factors of a number.

Rather than simply reason out how to find prime factors, I decided to adapt the code I found at [this site](https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/) and have it save the factors instead of printing them. This is definitely a problem that will make heavy use of unit testing to keep me sane. 

## What I Learned

### Generic

### Python

### Ruby

### Perl

