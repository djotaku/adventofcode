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

Answer: 786240

## Part 2
Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?

Answer: 831600

## Commentary / Approach to the Problem
### Part 1
Started off with the guess that: For any house the formula is -> Sum(F1*10+F2*10…..FN*10) where F is a factor of the number.  I think this means you can factor out the 10 and divide 10 from the number they give us. 

Did some non-AoC research (that is to say, I didn't look at anyone's solutions) and I think that meant I needed to compute the sum of divisors. [Here](https://mathschallenge.net/library/number/sum_of_divisors) is a site that explains that. Basically I need to find the prime factors of a number.

Rather than simply reason out how to find prime factors, I decided to adapt the code I found at [this site](https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/) and have it save the factors instead of printing them. This is definitely a problem that will make heavy use of unit testing to keep me sane. 
### Part 2
This one took me a little while and a ["shower thought"](https://www.urbandictionary.com/define.php?term=showerthought) to reason through, but once I did that it wasn't too hard. This time we needed to find all the factors, not just the prime factors. That way we could determine which elves (the elf number = one of the factors of the house number) were no longer on the job. Took about 30-60 minutes to run on my 6 core AMD that's a few years old. Wish on either part 1 or part 2 that I'd figured out how to shortcut myself to be in the vicinity of the right answer. Although I bet I could have sped either one up by dividing the puzzle input by 10 in the first and 11 in the second to arrive at an answer sooner. (Maybe? I'll have to think a bit more to see if that logic holds up.) 

### Optimization
After the terrible performance of my code, especially part 2, I [took to reddit to find a faster solution.](https://www.reddit.com/r/adventofcode/comments/po1zel/2015_day_20_there_must_be_a_more_efficient_way_to/?utm_source=share&utm_medium=web2x&context=3) The solution at [Python/part_2_optimized.py](https://github.com/djotaku/adventofcode/blob/77a4bf46514479adb7a37c39d243c1cb8c5480cd/2015/Day_20/Python/part_2_optimized.py) was a brilliant understanding of the math behind the elves who quit at 50 houses. It dropped my solution time from an hour to 2 seconds. Thank you reddit user ssnoyes for that one.

For part 1, the first thing I tried was a suggestion by user 2008p1990 which was supposed to run in 1-2 seconds. It seemed to run just as fast as my original part 1 so I did something that many folks do when "upping the ante" in AoC, I ran a profiler.  


## What I Learned

### Generic
How to calculate prime numbers and how to calculate the sum of divisors. 

### Python
- Nothing in particular, just putting together lots of skills I've learned before like using Counter and using math.prod to reduce the answer while multiplying.
### Ruby

### Perl

