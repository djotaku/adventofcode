# Day 11: Corporate Policy

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/11).

## Part 1

The previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, he has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for him, a new Security-person recently started, and he has imposed some additional password requirements:

- Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
- Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
- Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:

- hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
- abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
- abbcegjk fails the third requirement, because it only has one double letter (bb).
- The next password after abcdefgh is abcdffaa.
- The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

Given the current password (your puzzle input), what should his next password be?

Your puzzle input is hxbxwxba.

Answer: hxbxxyzz

## Part 2

It expired again, what's the next one?

Answer: hxcaabcc

## What I Learned for Each Language

In general, the second password took a while - along the order of a minute or so. So there's probably some efficient algorithm I'm not taking advantage of here.

### Python
- using ord() to get the ASCII value for a letter and then using that to advance to the next letter

### Ruby
- when it comes to password incrementing - Ruby naturally does the right thing. eg "az".next => "ba"
- Got more practice with chunk_while
- Used filter for the first time (as in the sequence: map, filter, reduce)
### Perl
-