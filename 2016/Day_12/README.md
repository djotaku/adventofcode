# Title of Problem

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/13).

## Part 1
The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's assembunny code designed for the new computer you just assembled. You'll have to execute the code and get the password.

The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and can hold any integer. However, it seems to make use of only a few instructions:

- cpy x y copies x (either an integer or the value of a register) into register y.
- inc x increases the value of register x by one.
- dec x decreases the value of register x by one.
- jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.

The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

For example:

- cpy 41 a
- inc a
- inc a
- dec a
- jnz a 2
- dec a

The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.

After executing the assembunny code in your puzzle input, what value is left in register a?

Answer: 318020

## Part 2
If you instead initialize register c to be 1, what value is now left in register a?

Answer: 9227674

## Commentary / Approach to the Problem
### Part 1
I tend to do well at these assembly language interpreter problems. Now that I have Python 3.10, I want to try their new switch-case syntax.

My Python solution for part 1 took a long time to run (relative to what was going on), but it did give me the right answer. Second time around, I removed the print statements. Apparently it took a long time because I was printing to the terminal.
## What I Learned

### Generic

### Python
- How to use match/case in Python
### Ruby

### Perl

### Go (Golang)

### Haskell
