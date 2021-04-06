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

# Lessons Learned

## Python

Nothing. This one was pretty easy.

## Ruby

- Began better understanding the .each syntax and how that works.
- Ends can get a bit tricky. I'd prefer Python where we're using whitespace or
Perl where we're using '{'
- Something about the way I imported my parser means that I just use the method name
and dont' include the filename.

## Perl 
- Ugh, a language with semicolons!
- Just like Python there are different comparison operators for different types.
I wasn't getting the right answer for part 1 until I changed from an == comparison to an eq comparison.
- Did not bother setting up a parser yet because I don't know how to make
Perl modules.