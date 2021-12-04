# Day 4: Giant Squid

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/4).

## Part 1
Playing bingo:

    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
    
    22 13 17 11  0
    8  2 23  4 24
    21  9 14 16  7
    6 10  3 18  5
    1 12 20 15 19
    
    3 15  0  2 22
    9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6
    
    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
    2  0 12  3  7

After 24 is called out:

the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Answer: 58412
## Part 2
Looks like it's time to "let the wookie win" (this is my commentary, based on what Eric Wastl has written here)

figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

Answer: 10030

## Commentary / Approach to the Problem
### Part 1
OK, so it looks like we need to program a bingo simulator. We have a few things I think I need to do (based on the way my brain works)

- Take care of the input to parse out boards and the bingo numbers that will be called
- Figure out how to represent the boards. Initial thought is to have a dictionary of dictionaries in which the inner dictionaries have keys being the (x,y) coords of the board. Then the value is a list where item 0 is the number and item 1 is whether that number wins
- Then I do a check after each number is called to see if a row wins
- Then calculate the score

I'm guessing there may be a simpler way where I don't need to keep track of whether a number has been called. Instead I can check all numbers that have been called so far against all rows and columns (I'm going to guess that part 2 is going to also consider diagonals). But it may be simpler logic to just do a check for what's already matched. Time will tell as I get into it. 

This is definitely going to be a problem where I will need some robust unit testing.

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
    