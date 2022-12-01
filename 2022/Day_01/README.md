# Day 1: Calorie Counting

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/1).

## Part 1
For example, suppose the Elves finish writing their items' Calories and end up with the following list:
```
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```
This list represents the Calories of the food carried by five Elves:

- The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
- The second Elf is carrying one food item with 4000 Calories.
- The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
- The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
- The fifth Elf is carrying one food item with 10000 Calories.

...like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Answer: 64929
## Part 2
How many Calories are those Elves carrying in total?

Answer: 193697
## Commentary / Approach to the Problem
### Part 1
In Python, at least, the approach for part 1 seems very simple. Parse the input and calculate a sum until you get to a newline.
Put this sum into a list. Use Python's max function to find the maximum number. Made easier by the fact that we don't care 
which elf has the calories, just the amount.
### Part 2
My approach to part 2, again using Python built-ins, is to sort the list and then pick the last 3 and sum those.
## What I Learned

### Generic

### Python
- Nothing, although I did have to refresh myself on parsing input and doing something with it rather than just parsing and dealing with it later.
### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    