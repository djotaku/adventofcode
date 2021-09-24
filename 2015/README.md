# Advent of Code 2015 - Santa's Weather Machine

Advent of Code 2015 can be found [here](https://adventofcode.com/2015).

I am coming to the 2015 problem set after having first done the 2020 problem set as my first year.

My goal for the 2015 problem sets are:

- Continue to reinforce my knowledge of idiomatic Python and solving common algorithms (ranked #2 on Github 2021Q1)
- To solidify my knowledge of Ruby, which I began learning last year (ranked #5 on Github 2021Q1)
- To reacquaint myself with Perl, which I haven't used in about a decade (ranked #21 on Github 2021Q1)
- In general my aim is to get more and more idiomatic with each language as the days go by.
- To have fun solving programming puzzles

![2015 ascii art](https://github.com/djotaku/adventofcode/blob/main/screenshots/2015_ascii_art_20210919.png)

## Days I could not complete
### Part 1 Sections Still incomplete:
### Part 2 Sections Still incomplete:

### Language Specific

#### Perl
- Day 7 - Because I was using recursion, and I had not yet relearned how to do subroutines (Perl functions)
- Day 14 - Because I didn't want to bother with classes in Perl

## What I learned from Advent of Code 2015

A distillation of what I learned this year.

- Perhaps this year I’m having a bit of hammer/nail disease, but having finally understood regex at the relatively simple level needed for AoC, I find that it makes nearly every problem infinitely easier compared to the way I did it in 2020 (mostly iterating over characters and keeping track of indexes, if needed)
- Confirmation of what I learned in 2020 - the right data structure is almost always the dictionary/hash. Nothing else is as performant.
- If you have recursion, you’ll probably have to do a cache to pass with the input given
- Looking like each year there’s at least one variant of Conway’s Game of Life - so learn the algorithm
- This year was a permutation/combination heavy year - many problems depended on knowing how to do that in your programming language


For a full list of what I learned, for each day the README will contain what I learned in each programming language.

### Python

- Got a lot more practice with regular expressions including learning when to use search vs match
- After struggling with it last December, I finally understand memoization
- using ord() to get the ASCII value for a letter and then using that to advance to the next letter
- How to do permutations where you need all the elements to sum to a specific number.
- How to use itertools Product to make combinations from different lists


### Ruby

- Creating files to import
- Using iterable#each to do idiomatic for loops
- map(&:to_i) to change an entire array from string to int without having to explicitly loop through the array.
- if $PROGRAM_NAME == __FILE__ to do Python’s equivalent of if __name__  == “__main__”
- How to do unit testing
- memoization/caching
- blocks in Ruby don't need something like pass, so I was just able to do if backspace_or_unicode == nil and keep going.
- string.delete_prefix and string.delete_suffix are the equivalent of lstrip and rstrip in Python
- Chunk and chunk_while - which made Day 10 so easy!
- Ruby classes and how to initialize them
- using sort to sort by custom variables in a class
- It appears you cannot just access variables in a Ruby class, you have to have a method to return the value. 
- How to do permutations where you need all the elements to sum to a specific number.
- array#flatten to reduce an array of arrays into an array
- by default, the Hash just returns nil instead of erroring out if I try to access a key that doesn't exist. Easier having to use get in Python.


### Perl

- Push instead of append to add to arrays
- sorting numerically is a lot more complicated in Perl than the other languages 
- using CPAN.
- Perl does not have True/False primitives
- Apparently there's no way to tell if something is a string. If it's not a number, hash, or array - it's a string
- The existence of the $-[0] and $+[0] after you do a regex match. They return the start and end of a match, respectively. 


## note to self

using toolbox to be able to install cpan and ruby gems without mucking with system.

Launch with:

toolbox enter adventofcode
