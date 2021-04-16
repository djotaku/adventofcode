# Day 5: Doesn't He Have Intern-Elves For This?

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/5).

## Part 1
A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
- It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
- It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

- ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
- aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
- jchzalrnumimnmhp is naughty because it has no double letter.
- haegwjzuvuyypxyu is naughty because it contains the string xy.
- dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

Answer: 255

## Part 2
None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

- It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
- It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

- qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
- xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
- uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
- ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

Answer: 55
## Commentary

- Looks like this is when I'm probably going to end up using regular expressions in all the solutions

## What I Learned

### Python
## Part 1
- The bool function - see rule 2.
- When to use findall vs search or match. Still slightly shakey, but I'm better at it than before.
- using back references to match doubles. My original rule 2 didn't work. 
- Been watching a lot of [this guy's](https://www.youtube.com/channel/UC1kBxkk2bcG78YBX7LMl9pQ) youtube channel so I was thinking in terms of map, filter, reduce (it's almost always the algorithm in the problems he solves). So that led to the code I had in the main function. 

## Part 2
- The key to rule 1 was to use find_all which automatically excludes overlaps. Then I just had to figure out the regex.
- using backslash and a number to refer to a repetition of a parenthesis'd number
### Ruby

### Perl