To read the story-version at AoC go [here](https://adventofcode.com/2015/day/1)

# Part 1

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

To what floor do the instructions lead?

Answer: 280

# Part 2

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes him to first enter the basement?

Answer: 1797
## Commentary / Approach to the Problem
(later fill in how you did this originally)

Coming at this in 2023 for another go-around with newer languages (like Go!), the best approach for part 1 would be to do a map then reduce. Map the parens to -1 and 1 and then sum. However, knowing what's coming in part 2, 
we can design the algorithm to do a for loop and store when we get to -1 and then keep on going.

# Lessons Learned

## Python

Nothing. This one was pretty easy.

## Ruby

- Began better understanding the .each syntax and how that works.
- Ends can get a bit tricky. I'd prefer Python where we're using whitespace or
Perl where we're using '{'
- Something about the way I imported my parser means that I just use the method name
and don't include the filename.
- [an alternate solution](https://github.com/djotaku/adventofcode/blob/main/2015/Day_01/Ruby/alternate_part_1.rb) for Ruby from /u/matheusrich on /r/ruby taught me how to use [reduce](https://docs.ruby-lang.org/en/3.0.0/Enumerable.html#method-i-reduce) in a way that seems to combine it with Python's enumerate

## Perl 
- Ugh, a language with semicolons!
- Just like Python there are different comparison operators for different types.
I wasn't getting the right answer for part 1 until I changed from an == comparison to an eq comparison.
- Did not bother setting up a parser yet because I don't know how to make
Perl modules.
- For Perl part 2 I used the "last" keyword to break out of the loop. First time using that.

## Go
- Just had to remember that running range on a string gives runes, not strings.