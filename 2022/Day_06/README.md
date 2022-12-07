# Day 06 - Tuning Trouble

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2022/day/6).

## Part 1
For example, suppose you receive the following datastream buffer:

mjqjpqmgbljsphdztnvjfqwrcgsmlb
After the first three characters (mjq) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. Because j is repeated, this isn't a marker.

The first time a marker appears is after the seventh character arrives. Once it does, the last four characters received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is complete after 7 characters have been processed.

Here are a few more examples:

- bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
- nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
- nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
- zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

How many characters need to be processed before the first start-of-packet marker is detected?

Answer: 1760
## Part 2
A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

- mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
- bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
- nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
- nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
- zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

- How many characters need to be processed before the first start-of-message marker is detected?
Answer: 2974

## Commentary / Approach to the Problem
### Part 1
The fact that we have a moving 4 character window screams limited size deque to me. 

Using a set to figure out if all characters were unique was an insight that surprised me, but kept the code extremely fast, including for part 2!
### Part 2
## What I Learned

### Generic

### Python
- Nothing
### Ruby

### Perl

### Go (Golang)

### Haskell

### Rust

### Julia
    