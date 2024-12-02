# Red-Nosed Reports

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2024/day/2).

## Part 1
Answer: 526
## Part 2

## Commentary / Approach to the Problem
### Part 1
When I saw today’s puzzle before heading off to work, I immediately thought of [2021 Day 01](https://github.com/djotaku/adventofcode/tree/1f6a3dcf738ed55ede1931847db2dbeee5e9fac6/2021/Day_01). In 2021 Day 01 the most efficient way to do the problem was to use a sliding “window” to do the math. However, as I went swimming and had nothing else to think about but the puzzle, I realized there were a few complications compared to that puzzle from 3 years ago. First of all, all the numbers in a row need to be going in the same direction (either all increasing or all decreasing). Second, I’m not just figuring out the difference - I need to keep it constrained to between 1 and 3 inclusive. 

My thought process for doing this is to tackle each constraint on its own. I don’t think this is the type of problem where that kind of inefficiency will cause issues. The second thing I was wondering if where I should stop early (as soon as I have an delta that’s outside of 1-3) or just wait until the end. Here’s the pseudo-code I’m considering:

Function 1:
Parameter: a list of numbers (need to remember to cast them to integers)
Create a sorted copy of the list. If the list matches we know they’re all increasing. Return True.
Create a reserve sorted copy of the list (or reverse the currently sorted copy depending on the language). If the list matches we know they’re all decreasing. Return True.
Function 2:
Parameter: a list of numbers 
Maybe using window (see zip solution in 2021 Day 01 README) calculate the absolute value of the delta between adjacent numbers. If you want to break early (maybe the row has a LOT of numbers?) you’ll probably need a for loop. Otherwise, at least in Python, you can just put True/False into a list. 
Return the value of all(list). This will either be True if they’re all True (all are 1-3 delta) or False if ANY of them fail.

Main:
Create placeholder variable (integer for languages that care)
Loop over the rows.
For each row If function1 AND function2 are true, add 1 to the placeholder variable.

Answer for part 1 is the placeholder variable value.

### Part 2
For part 2 I need to make both checks a little more complex. And I would need to make sure I'm only removing one of them. The only thing I can think of right now is the first check if I can fix the same direction bug and then fail on check delta. Then do the same in the other direction.
## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia

### Java

### Kotlin
    