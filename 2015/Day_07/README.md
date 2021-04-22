# Day 7: Some Assembly Required

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/7).

## Part 1
...he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

- 123 -> x means that the signal 123 is provided to wire x.
- x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
- p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
- NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i

After it is run, these are the signals on the wires:

    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

Answer: 956

## Part 2

## Commentary/Initial Strategies
- Put into dictionary with the key being whatever comes after ->
- Then we need a recursive function
    - To figure out the number for a letter, pull out what’s in that letter.
        - If it has a binary operator, try to figure out what each of those are
        - Unary - just try to figure out that one
    - Base case is the dictionary value being a number - then unwind the recursion
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
Until/unless I figure out how to get my Python solution to complete in < 13 hours, I'm not going to reimplement in Ruby. I think the issue is the algorithm.

### Perl
Until/unless I get to the section in Perl about subroutines (their version of functions) I'm not going to attempt the solution that requires recursion.