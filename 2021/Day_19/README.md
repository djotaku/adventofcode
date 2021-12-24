# Day 19: Beacon Scanner

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/19).

## Part 1
Assemble the full map of beacons. How many beacons are there?

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1
On 19 Dec I have NO IDEA how to even begin to understand this problem. I can't even understand how the 2D version works. I'm going to try and go back and solve some of the ones I couldn't solve while I was at Worldcon. 

I'm not sure when I'm going to come back to this, but I did [find a thread that helped me understand the 2D example](https://www.reddit.com/r/adventofcode/comments/rjrd0o/2021_19_part1_instructions_clarity/hp577mo/?utm_source=reddit&utm_medium=web2x&context=3). Essentially, the way to translate the points is to apply -5 to x and -2 to y. This allows all 3 points to match each other. By the time we get to the end of part 1, it turns out we don't need to find where the sensors are. We just need to figure out how many unique beacons there are. I think perhaps the way to do this is to transform all beacons to be from sensor 0's point of reference. Then we put them into a set and figure out how many are in the set. Easier said than done, I'm sure. 
## What I Learned

### Generic

### Python

### Ruby
- TBD
### Perl
- TBD
### Go (Golang)
- TBD
### Haskell
- TBD