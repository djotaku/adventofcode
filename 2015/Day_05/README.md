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
### Regular expressions
- Grouping with parenthesis and then using backslash to refer to that in order to do doubles.

For example:

```python
double_letter = re.compile(r'(.)\1')
    return bool(re.search(double_letter, string_to_eval))
```

There I'm saying find any character and then itself again. But it gets more fun in part 2.

```python
letter_pair = re.compile(r'(\w\w)\w*\1')
```

There I'm saying any 2 letters. Then 0 or more letters. Then the first two again. By using Python's findall, it doesn't do the overlap case 'aaa'. Then for part two, I had:

```python
regex = re.compile(r'(\w).\1')
```
There I've said one letter. Then exactly one other character (not necessarily a letter) then the same letter as before.

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
- An equivalent to the Python findall() with regular expressions is to use .scan on a string with an RE expression as the params. Then use a for loop to collect the number of times it matches.
- Many, MANY thanks to the folks who helped me on the [ruby subreddit](https://www.reddit.com/r/ruby/), especially [here](https://github.com/djotaku/adventofcode/blob/main/2015/Day_05/Ruby/part_1_more_rubyish.rb) where I learned:
    - if I want to force a bool, I could return !! expression or I could use .match? <- adding the question mark
	- Or should use assert instead of assert_equal(true, exp)
	- AND getting #<MatchData "aa" 1:"a"> was not an error, but the unit test telling me I'd succeeded
### Perl
- I probably could have gotten away with a slightly different if statement once I figured out the problem was rule 3. That said, I think I need the while loop to make sure I get all the counts of triple-vowels. 
- Also, a reminder to check for the opposite of a match to use !~
