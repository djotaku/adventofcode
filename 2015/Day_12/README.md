# Day 12: JSAbacusFramework.io
Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/12).
## Part 1

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

- [1,2,3] and {"a":2,"b":4} both have a sum of 6.
- [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
- {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
- [] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

Answer: 156366

## Part 2

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

- [1,2,3] still has a sum of 6.
- [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
- {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
- [1,"red",5] has a sum of 6, because "red" in an array has no effect.

Answer: 96852

## What I learned in each Language

### Python

### Ruby

### Perl
