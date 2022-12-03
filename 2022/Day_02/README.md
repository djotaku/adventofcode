# Day 02 - Rock Paper Scissors

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/2).

## Part 1
You get a score for the shape you play and whether that resulted in a win, loss, or draw.

The strategy guide tells you what shape to play.

For example, suppose you were given the following strategy guide:
```
A Y
B X
C Z
```
This strategy guide predicts and recommends the following:

- In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
- In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
- The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

Answer: 13446
## Part 2
Turns out the strategy guide actually tells you whether to win, lose, or draw.



Answer: 13509
## Commentary / Approach to the Problem
### Part 1
A function/subroutine to calculate the score for the strategy used. Another function to determine if you won.

### Part 2
I need to run things in reverse, but I think I can keep the functions I already made.

Now that the entire problem has been revealed to me, I'm going to create a dictionary/hash/map with all the possible outcomes and scores. Then I can just reference that dictionary. 
## What I Learned

### Generic
- Once again, setting things up during input phase makes less of a headache.
### Python
- Nothing
### Ruby

### Perl

### Go (Golang)
- Practice with maps of maps
- A reminder of the strings.Fields to do the equivalent of Python's split() 

### Haskell

### Rust

### Julia
    
