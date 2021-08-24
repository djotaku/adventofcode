[Cute Version](https://adventofcode.com/2020/day/3)

# Part 1

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many hashes would you encounter?

# Part 2

traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 hash(es) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of hashes encountered on each of the listed slopes?