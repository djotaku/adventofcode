# Day 23: Opening the Turing Lock 

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/23). 

## Part 1
the computer supports two registers and six instructions The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

- hlf r sets register r to half its current value, then continues with the next instruction.
- tpl r sets register r to triple its current value, then continues with the next instruction.
- inc r increments register r, adding 1 to it, then continues with the next instruction.
- jmp offset is a jump; it continues with the instruction offset away relative to itself.
- jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
- jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

  inc a
  jio a, +2
  tpl a
  inc a

What is the value in register b when the program in your puzzle input is finished executing?

Answer: 307

## Part 2
what is the value in register b after the program is finished executing if register a starts as 1 instead?

Answer: 160

## Commentary / Approach to the Problem
This is a relatively simple assembly language sim. There was also at least one of these problems in the 2020 problem set. Unless I'm missing something key about part 1 it should be as simple as moving along a list, running commands.

I went back and forth on whether to use regular expressions or split methods. In the end the complexity seemed similar no matter which I chose, so I went with splits. Very easy solution for both parts 1 and 2. I think Wastl was trying to give folks a break.
## What I Learned

### Generic

### Python
- Nothing

### Ruby
- practiced with case statements. They can get a little dodgy when they're nested. Also had to be careful with the insistence on an "else"
### Perl
- When you do a chop, what's returned is what's removed. So you need to do a chop before the comparison
