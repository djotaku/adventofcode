# Day 7: Some Assembly Required

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/7).

## Part 1

## Part 2

## Commentary/Initial Strategies
- Put into dictionary with the key being whatever comes after ->
- Then we need a recursive function
    - To figure out the number for a letter, pull out what’s in that letter.
        - If it has a binary operator, try to figure out what each of those are
        - Unary - just try to figure out that one
    - Base base is the dictionary value being a number - then unwind the recursion
- Helper function for recursive function -> parse the instruction (or maybe it’s easier for this to be in recursion - will have to test)
    - Need to figure out if it’s unary or binary - one thing that might help with regex is that all the commands are uppercase and the wires are all lowercase
        - I think first you look for uppercase
        - Then a case statement or if/else that keys in on that to figure out what to do - like if it’s a unary or binary function
        - If there is no uppercase there 2 possibilities:
            - It could be the number leading to the wire
            - OR it could be just a fallthrough - we have that in the input where some other wire just leads straight to wire a

## What I learned

### Python

### Ruby

### Perl