# What I learned on Day 09 in Perl

## Part 1
- how to create a subroutine
- how to pass an arrays and hashes to a subroutine
    - I have to say that this is the most frustrating system between Perl, Python, and Ruby for passing items in. It really is annoying to figure out what is the right thing to do to accurately grab from the @_ or $_ or even if you should be using one or the other. Guess I'm going to learn over the next few problem sets. Yeesh! (The day after I wrote this, I went over the chapter in Programming Perl that explains it a little better. I think I have it now.)
    - while using subroutines in Perl forced me to wrap my head around the weird way Perl thinks with passing in arrays and hashes, I did like how much easier it was to make my hash of hashes than it was in Python (or Ruby) where I had to first check if it was in the dict (or hash). 
- constantly changing the symbol from @ or % to $ is annoying
- ```my %index_dictionary = %city_dict_keys[0..$#city_dict_keys];``` aka Perl slices - requires v5.20
- Permutations (and, by extension, generators) in Perl
- Note to self: Requires toolbox as it makes use of an installed CPAN module [Algorithm::Permute](https://metacpan.org/pod/Algorithm::Permute)
- use List::Util qw(min); and qw(max)

## Part 2
- Nothing
