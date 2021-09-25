# Day 5: Binary Boarding

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/5).

## Part 1

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

Answer: 890

## Part 2

It's a completely full flight, so your seat should be the only missing boarding pass in your list.

What is the ID of your seat?

Answer: 651

## Commentary / Approach to the Problem
When I did this in 2020, I didn’t realize that Wastl was essentially giving us a binary representation of our seat number. Instead I created a version of the guessing game (one of the first games you usually program when learning how to program games) where each F and B narrowed the search space. When I come back to this with other programming languages I intend to do the binary solution.
## What I Learned

### Generic

### Python

### Ruby

### Perl

