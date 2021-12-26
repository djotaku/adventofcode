# Day 25: Sea Cucumber

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/25).

## Part 1
There are two herds of sea cucumbers sharing the same region; one always moves east (>), while the other always moves south (v). Each location can contain at most one sea cucumber; the remaining locations are empty (.).

Every step, the sea cucumbers in the east-facing herd attempt to move forward one location, then the sea cucumbers in the south-facing herd attempt to move forward one location. When a herd moves forward, every sea cucumber in the herd first simultaneously considers whether there is a sea cucumber in the adjacent location it's facing (even another sea cucumber facing the same direction), and then every sea cucumber facing an empty location simultaneously moves into that location.

So, in a situation like this:

    ...>>>>>...
After one step, only the rightmost sea cucumber would have moved:

    ...>>>>.>..
After the next step, two sea cucumbers move:

    ...>>>.>.>.
During a single step, the east-facing herd moves first, then the south-facing herd moves.

What is the first step on which no sea cucumbers move?

Answer: 
## Part 2

## Commentary / Approach to the Problem
### Part 1
This seems a relatively easy simulation. For each step attempt to move east and then south. The biggest complications appear to be the fact that it wraps around.


## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
