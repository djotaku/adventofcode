# Day 13: Shuttle Search

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/13). 


## Part 1

In the example: 

The earliest bus you could take is bus ID 59. It doesn't depart until timestamp 944, so you would need to wait 944 - 939 = 5 minutes before it departs. Multiplying the bus ID by the number of minutes you'd need to wait gives 295.

What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?

Answer: 3246

## Part 2

find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute.

For example, suppose you have the same list of bus IDs as above:

7,13,x,x,59,x,31,19

An x in the schedule means there are no constraints on what bus IDs must depart at that time.

This means you are looking for the earliest timestamp (called t) such that:

- Bus ID 7 departs at timestamp t.
- Bus ID 13 departs one minute after timestamp t.
- There are no requirements or restrictions on departures at two or three minutes after timestamp t.
- Bus ID 59 departs four minutes after timestamp t.
- There are no requirements or restrictions on departures at five minutes after timestamp t.
- Bus ID 31 departs six minutes after timestamp t.
- Bus ID 19 departs seven minutes after timestamp t.

Answer: 

## Commentary / Approach to the Problem
### 2020

### 2021
For 2021 I decided to simply approach part 2 of the problem. This didn't seem like one where the second answer was going to really depend all too much on the solution to the first one.

I started off with the following idea for solving it: 

"I think this involves Greatest Common Multiple or something like that. Or maybe greatest Common Multiple PLUS 1 for each index distance from the first bus."

That didn't yield results so I decided to try and brute-force it.
## What I Learned

### Generic

### Python

### Ruby

### Perl

