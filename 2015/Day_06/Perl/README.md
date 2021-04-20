# What I learned on Day 06 from Perl

## Part 1
- how to do ranges in Perl. Although I had to abandon it for a C-style for-loop to get my coordinates.
- using hashes. 
- For starting an empty array, I need to just use
```perl
my @array;
```
When I did:
```perl
my @array = []; 
```
[I ended up with an extra light being counted](https://github.com/djotaku/adventofcode/blob/525e2e0bb5aaa1e3412d508aaf4c3342ef9ce6dc/2015/Day_06/Perl/part_1.pl). Thanks to /u/its_a_gibibyte for helping me out on [/r/adventofcode](https://www.reddit.com/r/adventofcode/)
- my final part 1 solution needs List::Util so install from CPAN 
## Part 2
