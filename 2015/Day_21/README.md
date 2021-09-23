# Day 21: RPG Simulator 20XX

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/21).

## Part 1
In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

    Weapons:    Cost  Damage  Armor
    Dagger        8     4       0
    Shortsword   10     5       0
    Warhammer    25     6       0
    Longsword    40     7       0
    Greataxe     74     8       0

    Armor:      Cost  Damage  Armor
    Leather      13     0       1
    Chainmail    31     0       2
    Splintmail   53     0       3
    Bandedmail   75     0       4
    Platemail   102     0       5

    Rings:      Cost  Damage  Armor
    Damage +1    25     1       0
    Damage +2    50     2       0
    Damage +3   100     3       0
    Defense +1   20     0       1
    Defense +2   40     0       2
    Defense +3   80     0       3

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

Answer: 91


## Part 2
What is the most amount of gold you can spend and still lose the fight? 

Answer: 

## Commentary / Approach to the Problem
I spent a lot of time thinking about how to work this one. I thought about how to brute force it and how to come up with an algorithm. I thought about Combinations or Permutations. 

Eventually what I ended up doing was coming up with dictionaries (also called maps or hashes in other languages) to hold the weapon, armor, and ring data. Then I used itertools Product to combine them into groups I could test. I think the biggest innovation I had was to create NoMail and NoRing to represent not wearing armor or rings. And to have rings go into product twice to handle it being one or both hands. 

I decided to do everyting out of dictionaries (including the player and boss) rather than classes to make it easy to do this in any programming language. 

## What I Learned

### Generic

### Python
- How to use itertools Product to make combinations from different lists
- A reminder the generators are consumed
### Ruby
- a reminder about array#min and array#max rather than the if statements to determine the value to keep. May be

### Perl
- using Math::Cartesian::Product
- more experience with hashes
- more practice using last to break out of a loop in Perl

