# Day 8: Handheld Halting

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/8).

## Part 1


    acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
    jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
    nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

Immediately before any instruction is executed a second time, what value is in the accumulator?

Answer: 1553

## Part 2

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

Answer: 1877

## Commentary / Approach to the Problem

## What I Learned
### Part 1
A relatively simple assembly language sim. I actually like the elegance of my solution here splitting out the interpretation of the command into its own function. I wish I’d done this during the 2015 ASM sim problem - it would have made debugging much less annoying because I’d be looking at a smaller chunk of the code. 

### Part 2
Once again, a relatively simple modification to the code for part 2

### Generic

### Python

### Ruby

### Perl

