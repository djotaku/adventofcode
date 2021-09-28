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

Answer: 1010182346291467 

## Commentary / Approach to the Problem
### 2020
Overall a simple, if relatively inefficient search to find the earliest bus to take me to the airport. 

### 2021
For 2021 I decided to simply approach part 2 of the problem. This didn't seem like one where the second answer was going to really depend all too much on the solution to the first one.

I started off with the following idea for solving it: 

"I think this involves Greatest Common Multiple or something like that. Or maybe greatest Common Multiple PLUS 1 for each index distance from the first bus."

That didn't yield results so I decided to try and brute-force it.

- [My first attempt too a long time, even with the pytest input.](https://github.com/djotaku/adventofcode/blob/2e71688de9f467534714e4de4519c76778f9c916/2020/Day_13/Python/2021/part_2.py)
- [My second attempt was blazing fast in pytest, but still slow for main input](https://github.com/djotaku/adventofcode/blob/bdc91a7d4f640f66b4a246abcf8532e54718093b/2020/Day_13/Python/2021/part_2.py)

I kept trying variations on GCD and LCM, but I couldn't find anything that would modulo cleanly with the answer for the unit test. This would give me a faster way to count up than by the first number. (Counting up by the largest number didn't work.)

[Eventually I found an attempt that was very fast for the sample input, but wouldn't complete for the given input.](https://github.com/djotaku/adventofcode/blob/2a2f3c6e61cbbadfc37cf7dde7c7d14740c85381/2020/Day_13/Python/2021/part_2_good_and_fast_for_sample_would_not_finishi.py)

I had to copy the above solution, which I was very proud of (using all(), for example), into a new file because I wanted to get back to the blazing fast code (second link here in part 2) to get to the an adaptation of the code I found [here](https://www.reddit.com/r/adventofcode/comments/kc4njx/comment/gktms17/?utm_source=share&utm_medium=web2x&context=3).  Once I had reached this point and realized that my code would never finish, I was trying to figure out how to increase my increments as I solved the for successive buses, but I couldn't figure out how to do it.

So I went onto the AoC subreddit and learned a few things, including the fact that most folks recommended using Chinese Remainder Theorem. I didn't understand it in 2020 or now in 2021. I did come across a really funny post where someone said they came up with a solution because they couldn't understand CRT and someone pointed out he'd actually just reinvented CRT from first principles. I also tried to merge buses for a while after seeing that as a solution, but I was never able to make that work. 

The things that I see as key for the solution that I adapted from the code linked above is that:
- I had to move the code out into a function so that I could better have it be a condition for the while loop while being outside the while loop
- the determine_interval function which was the key piece of the puzzle for me. It's how he tracked and implemented the ability to increase the interval. It ends up causing the solution to be solved nearly instantaneously on my computer.  

## What I Learned

### Generic

### Python

### Ruby

### Perl

