# Day 17: Trick Shot

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/17).

## Part 1v
The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

- The probe's x position increases by its x velocity.
- The probe's y position increases by its y velocity.
- Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
- Due to gravity, the probe's y velocity decreases by 1.

For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be within a target area after any step. The submarine computer has already calculated this target area (your puzzle input). For example:

target area: x=20..30, y=-10..-5

This target area means that you need to find initial x,y velocity values such that after any step, the probe's x position is at least 20 and at most 30, and the probe's y position is at least -10 and at most -5.

Answer: 


## Part 2

## Commentary / Approach to the Problem
### Part 1

The "after any step" confused me at first. But basically it just means that EVENTUALLY it needs to be somewhere in the target zone. This seems DECEPTIVELY easy. My initial approach is:

- Design a function to take a current x,y position and velocity. Calculate teh new position and velocity and return it.
- Need a function or while loop or something to check it the probe ever gets there.

Although, thinking about it now - perhaps it makes more sense to start somewhere in your target area and reverse engineer getting back to 0,0?

Or do we just use the quadratic equation to solve for a parabola? That might be too hard because of the drag and gravity effects. 

Oh, wait, I think I might know...

d = vt + 0.5a(t^2)

a for y is -1 and also for x (at least until it reaches 0) Not sure this helps me since they don't give a specific time point.

The example for 6,3 shows that it's not quadratic since you can end up just going straight down. So I'm left unsure of how to solve this without just going through all the points.

But thinking about ways to know if I've chosen a bad velocity:
- v_x becomes 0 and we're not within 20-30
- y position is below -10 (above doesn't matter since it'll always fall)

So I think I've decided that I will just simulate various x and y velocities and have a stopping point if they can't reach their destination.



## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
