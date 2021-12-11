# Day 9: Smoke Basin

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/9).

## Part 1
Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Answer: 577.

## Part 2
A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

The top-right basin, size 9:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

Answer; 1069200.

## Commentary / Approach to the Problem
### Part 1
This actually doesn't seem too hard. My plan is to do what I did for Conway in the 2015 problem set - create a dictionary to represent points. Then I can go through each point and check its neighbors to see if it's a minima. Dictionaries help along the edges and corners because they're a lot less work than a list to check.  Speaking of Conway, curious if that ends up being part 2 - some kind of smoke modeling.

So this may be a little complex given how large the input is. I'll DEFINITELY need to use a unit test to make sure I'm getting the indexes, neighbors, etc right. Overall doesn't seem too hard, just more work than I can do before starting my day today.  

Overall the answer was relatively easy to calculate without any issues.

### Part 2
After reading the problem statement twice, it looks like what I need to do is flow from a low point out in all directions until hemmed in by 9s.  

That part I'm worried about it:

"all other locations will always be part of exactly one basin"

What was so easy to state turned out to be complicated to turn into an algorithm. I dont' know if it would be presumptuous of me to say that I "accidentally" reinvented the tree search (because I can't remember enough of my algorithms class from nearly 20 years ago to say for sure), but I got a nice, recursive solution that works!

## What I Learned

### Generic

### Python
- The correct way to put two sets together is set = set.union(set1, set2)
### Ruby
- TBD
### Perl
- TBD
### Go (Golang)
- TBD
### Haskell
- TBD