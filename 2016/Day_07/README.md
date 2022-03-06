# Day 7: Internet Protocol Version 7

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/7).

## Part 1
An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

- abba[mnop]qrst supports TLS (abba outside square brackets).
- abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
- aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
- ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?

Answer: 115

## Part 2
An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

- aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
- xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
- aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
- zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

Answer:

## Commentary / Approach to the Problem
### Part 1
Once again, 2015 Day 5 might help because it showed how to look for letters in certain patterns. Idea is to evaluate each line against the 3 rules we know, eliminating any that don’t pass all three rules.
- ABBA
- A and B are different
- ABBA not found in brackets

### Part 2
First of all, initial assumption is that I'm not starting from the 115 that I found, but going back to the original set. That's what the wording leads me to believe is the right answer.

Second, I'm going to try and construct a regex that can get this in one shot. Or at the very least, can get me most of the way there and I just need to eliminate the "aaa" situation.
## What I Learned

### Generic
- used the awesome regex101.com to figure out the regex expressions for the rules
### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
