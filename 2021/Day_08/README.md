# Day 8: Seven Segment Search

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/8).

## Part 1
Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....
    
      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

Answer: 548

## Part 2
For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

Answer: 

## Commentary / Approach to the Problem
### Part 1
Going into part 1 I was afraid Wastl was asking us to do what he'd eventually ask us to do in Part 2. In the end it turned out to be incredibly simple. Just look at the second half (after the | ) and and see if the lengths matched the magic values.

[Part one answer.](https://github.com/djotaku/adventofcode/blob/46276bbb1864991d5296a78587b5864e88a33e68/2021/Day_08/Python/solution.py)

### Part 2

Ugh, I always hate these kinds of problems. Couldn't solve the allergen one in 2020 either. I worked literally 2 hours on this. As my if statements were getting crazier, I knew I was DEFINITELY on the wrong path and coming up with something that couldn't be debugged. I gave up with [this code](https://github.com/djotaku/adventofcode/blob/655b3b9c38289037b6ac0c5f2d95731758311af0/2021/Day_08/Python/solution.py) and decided to check the megathread. (Also working together with a coworker whose coding skills I respect, who also got stuck on this one. Made me feel less bad.)

First answer (at the time I checked) was a Python golf that meant nothing to me. User /u/ho0ber came upw ith:

```python
from collections import*
y=z=0
u=frozenset
for l in open(0):S,O=l.split("|");c=Counter(S);m={u(s):[42,17,34,39,30,37,41,25,49,45].index(sum(c[x]for x in s))for s in S.split()};o=[str(m[u(o)])for o in O.split()];y+=sum(x in"1478"for x in o);z+=int("".join(o))
print(y,z)
```

Luckily, just a bit further down I [found a solution that I could use to learn from](https://www.reddit.com/r/adventofcode/comments/rbj87a/comment/hnr3uau/?utm_source=share&utm_medium=web2x&context=3). I then adapted this to my code so that I could learn (and also because I don't have 3.10 yet, so no match statements.)

## What I Learned

### Generic

### Python

### Ruby
- TBD
### Perl
- TBD
### Go (Golang)
- TBD
### Haskell
- TBD