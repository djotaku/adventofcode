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
- Thanks to helpful folks on the subreddit (grnngr and NeilNjae), they confirmed I should use json. Then they helped me with my recursion issues by providing some more unit test cases.
### Ruby
- each_pair for Hashes - equivalent to Python's dict.values()

### Perl
- use Scalar::Util qw(looks_like_number) to figure out if something is a number
- using ref($scalar) eq "ARRAY" or ref($scalar) eq "HASH" to tell if they are hashes
- Apparently there's no way to tell if something is a string. If it's not a number, hash, or array - it's a string. So I ended up eliminating the string check that I had in Ruby and Python because it wasn't working well. 
- the same way that you can do (keys %hash), you can also do (values %hash)
- the JSON::PP library (which is built-in)
