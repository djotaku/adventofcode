# Day 4: Passport Processing

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/4).

## Part 1

The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Count the number of valid entries - those that have all required fields. Treat cid as optional.

Answer: 

## Part 2

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the inputs where all required fields are both present and valid according to the above rules.

Answer: 

## Commentary / Approach to the Problem
I recently watched a video in which the Kotlin devs solved this problem in Kotlin. On the plus side, my solution wasn't too far off from theirs. But I'm definitely making this slightly more complex than it has to be by involving sets. Still, I'm relatively proud of myself for this solution. 

## What I Learned

### Generic

### Python
- Nothing

### Ruby

### Perl

