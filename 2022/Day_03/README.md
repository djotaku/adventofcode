# Day 3 - Rucksack Reorganization

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/3).

## Part 1

Answer: 8088
## Part 2
Answer: 2522
## Commentary / Approach to the Problem
### Part 1
 -Use normal multiple lines in function
- For loop for the next part 
- Cut string in half (or use enumeration -or language equivalent to know when you're at the halfway point. If doing this, skip to next step)
- Go over each letter per half of string and put it into a set
- Set subtraction tells you which letter is by itself
- Put the letter into a list that's outside this for loop
- Using a letter-value dictionary, figure out what each letter is worth (Ruby and Haskell can probably use map function for this. Python can use list compensation or map)
Sum

### Part 2
I think I can do a modified version of what I was doing above, only with lines instead of halves of lines. And comparing 3 lines. 
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    