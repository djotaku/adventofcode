# Day 22: Wizard Simulator 20XX

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/22).

## Part 1
Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

- Magic Missile costs 53 mana. It instantly does 4 damage.
- Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
- Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
- Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
- Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

What is the least amount of mana you can use and still win the fight: 

Answer: 953

## Part 2

## Commentary / Approach to the Problem
- Important that no matter the amount of defense, always at least 1 HP is taken away per attack
- Also, there are 2 lose conditions - 0 HP and 0 MP
- I *think* the best strategy is to have some guards running - you can’t lose too much HP OR mana. So, need to make sure that if you only have 229 left that you cast Recharge. Also, figure out when to do shield or drain. Finally, when do you do Magic Missile or Poison? 

  - If reach 2 HP cast shield
  - If reach 1 HP cast Drain
  - If 229 MP left, cast Recharge (or at start like in example?)
  - If none of these needed, Poison
  - If poison already in effect, Magic Missile
  - Also a check to make sure don’t cast anything already running -> have Bools related to each spell running -> put it into the dict for the spell?

Ended up having to abandon any kind of  
## What I Learned

### Generic

### Python

### Ruby

### Perl

