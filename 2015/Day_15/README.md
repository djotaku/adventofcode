# Day 15: Science for Hungry People

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/15)

## Part 1

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

- capacity 
- durability
- flavor
- texture
- calories

You can only measure ingredients in whole-teaspoon amounts accurately. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

- Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
- Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

- A capacity of 44*-1 + 56*2 = 68
- A durability of 44*-2 + 56*3 = 80
- A flavor of 44*6 + 56*-2 = 152
- A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

Answer: 21367368

## Part 2

Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

Answer: 1766400

## Commentary

What I was intending as my original approach before someone on AoC told me it was easy to brute force since it wasn't too many values:

- Each cookie is a dict of dicts or named tuple -> All we care about is the final, multiplied number. Might be easier to just have a list of lists. Each sublist represents one of the ingredients. Then we can multiply by the list and use zip (or something…) to add together the ingredients that go together.
- Looking at each ingredient in my list shows that each one has one property that would lead to a score of 0 because it’s either 0 or negative
  -Therefore start with 25 of each 
  - Store current score
  - For each ingredient, increase it at the cost of the others (how exactly? Which one do I subtract from?)
  - If I get to a score of 0 (which will happen because each one has negative numbers):
      - Go back one
      - Compare current score with stored score. If higher: replace score and ingredient composition with current if new high score
  - Go on to the next ingredient (but do I start from 25 again or from where I’m at now?) And repeat

## What I learned in each language

### Python
- How to do permutations where you need all the elements to sum to a specific number.
- A little more practice with the zip function

### Ruby
- Permutations in Ruby, along with how to filter them
- A better understanding of Enumerators in Ruby being like Iterators in Python and how to make them go faster - see the Ruby specific readme.md for today to see my learning process for this
- array.transpose
- array.select

### Perl
