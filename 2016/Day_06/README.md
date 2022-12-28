# Day 6: Signals and Noise

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/6).

## Part 1
All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

    eedadn
    drvtee
    eandsr
    raavrd
    atevrs
    tsrnev
    sdttsa
    rasrtv
    nssdts
    ntnada
    svetve
    tesnvt
    vntsnd
    vrdear
    dvrsen
    enarar

The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

Answer: dzqckwsd

## Part 2
In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

Answer: lragovly.

## Commentary / Approach to the Problem
### Part 1
My initial approach to the problem: For each position, have a Count dict (or tally hash in Ruby or map/hash in Go/Perl) and then have it spit out #1 for each position. Should actually be a lot easier than Day 4 part 2.

#### Go
I decided to try and design an answer with basic Go libraries, not importing something like https://github.com/ekzhu/counter

## What I Learned

### Generic

### Python
- Counter does not have a least_common method - boo!
### Ruby

### Perl

### Go (Golang)

### Haskell
