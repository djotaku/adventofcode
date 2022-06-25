# Explosives in Cyberspace

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/9).

## Part 1
The format compresses a sequence of characters. Whitespace is ignored. To indicate that some sequence should be repeated, a marker is added to the file, like (10x2). To decompress this marker, take the subsequent 10 characters and repeat them 2 times. Then, continue reading the file after the repeated data. The marker itself is not included in the decompressed output.

If parentheses or other characters appear within the data referenced by a marker, that's okay - treat it like normal data, not a marker, and then resume looking for markers after the decompressed section.

For example:

- ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
- A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
- (3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
- A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
- (6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
- X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.

What is the decompressed length of the file (your puzzle input)? Don't count whitespace.

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1

The hard part here is that we can have parenthesis within the parenthesis so we can't juse use a regex. 

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
