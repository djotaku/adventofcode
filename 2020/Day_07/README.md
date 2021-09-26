# Day 7: Handy Haversacks

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/7)

## Part 1

consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag?

Answer: 119

## Part 2

Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

Answer: 155802

## Commentary / Approach to the Problem
### 2020
#### Part 1
This is quite a mess. 105 lines of code vs my 2021 solution in 47. I create a CLASS for my bags to hold parents and children. This was very over-engineered. Because I wasn't any good at regular expressions, I've got this crazy function for finding the adjective color. My main for loop is also nuts. I've evolved quite a big with Python in the past year.
#### Part 2
Continues the mess from part 1 and never was able to get the right answer. 

### 2021
#### Part 1
The solution was incredibly easy given how comfortable I've become with regular expressions. It was very easy to use re.findall to find all instances of the pattern on the bag descriptions. This spared me from my initial inclination of splitting the container bag and also having conditionals on whether there were commas. 

After that it was very easy to write a recursive algorithm to count bags that had a gold bag somewhere inside them.
#### Part 2
In 2020 I was never able to write a working solution. In 2021 I was able to make better use of my understanding of dictionaries and caching to write a solution that finishes incredibly quickly. 

It was nice to finally solve this problem. 

### Comparison of cProfile/Runtime 2020 vs 2021 Part 1
- 2020 completion time - 0.632 seconds
- 2021 completion time - 0.023 seconds

## What I Learned

### Generic

### Python

### Ruby

### Perl

