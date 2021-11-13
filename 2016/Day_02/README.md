# Day 2: Bathroom Security

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/2).

## Part 1
The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

    ULL
    RRDDD
    LURDL
    UUUUD

- You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
- Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
- Continuing from "9", you move left, up, right, down, and left, ending with 8.
- Finally, you move up four times (stopping at "2"), then down once, ending with 5.

So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?

Answer: 69642

## Part 2
...the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

      1
    2 3 4
  5 6 7 8 9
    A B C
      D

Using the same instructions in your puzzle input, what is the correct bathroom code?

Answer: 8CB23


## Commentary / Approach to the Problem
### Part 1 ###
The problem was very simple in Python. I created a multidimensional array to hold the keypad and then a simple helper function to figure out where we were in the array. 

### Part 2 ###
For part 2, I decided to go with some slightly tortured logic and stick to the array. If that gets too unwieldly, I'll try a different approach. 

And it did indeed get [too unweildly](https://github.com/djotaku/adventofcode/blob/c57c1367ff5b35b0b0a003aacf99c938c0c2c783/2016/Day_02/Python/part_2.py). So I came up with an idea that could be generalizable to create a solution that works for both parts 1 and 2. I created a set with valid coordinates and then only changed the key_y and key_x values if the new coordinate was in the set of valid coordinates.

## What I Learned

### Generic

### Python
- Nothing new this time around. 
### Ruby
- Nothing new this time around.
### Perl
- Nothing really, but did get a bit better at arrays in Perl
### Go (Golang)
- global variables
- using the sets package someone else created
- how to iterate over a string and since it makes runes, have to use single quotes when comparing
- Go arrays/slices are a pain in the ass since they need to only be of one type!
### Haskell
- Type of quotation matters for thinking of a char or a string. A string has double quotes and a char has single quotes. See [this](https://github.com/djotaku/adventofcode/blob/800175cb4e0a69cb8d15e88d0727a07e7108fd8d/2016/Day_02/Haskell/solution.hs) vs [this](https://github.com/djotaku/adventofcode/blob/61b3be4b88df14ffb06ede25c272be928c06cd40/2016/Day_02/Haskell/solution.hs)
- making creative use of othewise to shorten the function to find the next keypad entry
