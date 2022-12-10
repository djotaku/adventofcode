# Day 10 - Cathode-Ray Tube

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/10).

## Part 1
Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:

- addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
- noop takes one cycle to complete. It has no other effect.

The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.

Consider the following small program:
```
noop
addx 3
addx -5
```
Execution of this program proceeds as follows:

- At the start of the first cycle, the noop instruction begins execution. During the first cycle, X is 1. After the first cycle, the noop instruction finishes execution, doing nothing.
- At the start of the second cycle, the addx 3 instruction begins execution. During the second cycle, X is still 1.
- During the third cycle, X is still 1. After the third cycle, the addx 3 instruction finishes execution, setting X to 4.
- At the start of the fourth cycle, the addx -5 instruction begins execution. During the fourth cycle, X is still 4.
- During the fifth cycle, X is still 4. After the fifth cycle, the addx -5 instruction finishes execution, setting X to -1.

For now, consider the signal strength (the cycle number multiplied by the value of the X register) during the 20th cycle and every 40 cycles after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?

Answer: 15880

## Part 2

Answer: PLGFKAZG
## Commentary / Approach to the Problem
### Part 1
I think the trickiest thing here is that some of the instructions take 2 cycles. So it can't just be a simple loop. 

I think it might help to return the signal strength on every tick and then just deal with it if it's modulo 20.

Perl has the ability to go back to the top of a loop, wonder if that would be helpful here.

After working it for a while, Since it's 20th and then 40 after that, it's not easy to use modulo. Will go to manually coding the cycle values.
### Part 2

## What I Learned

### Generic

### Python
- Nothing
### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    