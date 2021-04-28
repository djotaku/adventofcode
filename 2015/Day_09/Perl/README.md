# What I learned on Day 09 in Perl

## Part 1
- how to create a subroutine
- how to pass an arrays and hashes to a subroutine
    - I have to say that this is the most frustrating system between Perl, Python, and Ruby for passing items in. It really is annoying to figure out what is the right thing to do to accurately grab from the @_ or $_ or even if you should be using one or the other. Guess I'm going to learn over the next few problem sets. Yeesh!
- constantly changing the symbol from @ or % to $ is annoying
- ```my %index_dictionary = %city_dict_keys[0..$#city_dict_keys];``` aka Perl slices - requires v5.20
- 
