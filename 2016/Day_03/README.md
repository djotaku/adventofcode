# Day 3: Squares With Three Sides

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/3).

## Part 1
In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

Answer: 1050
## Part 2
...triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

   101 301 501
   102 302 502
   103 303 503
   201 401 601
   202 402 602
   203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

Answer: 1921
## Commentary / Approach to the Problem
I went into part 1 with the attitude/belief: Seems easy as valid_triangle function that evaluates the numbers, summing all the pairs and returning false if any is < the length of the third one.

That worked out just fine. Part 2 was about figuring out the best way to manipulate the input. It wasn't too bad, although I think I wasn't as efficient as I could have been.
## What I Learned

### Generic

### Python
- Nothing
### Ruby
- Array.transpose
### Perl
- Nothing
### Go (Golang)
- Using string.Fields to get space-separated text from a string
### Haskell
