# Day 6: Custom Customs

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2020/day/6).


## Part 1

    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b

This list represents answers from five groups:

- The first group contains one person who answered "yes" to 3 questions: a, b, and c.
- The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
- The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
- The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
- The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Answer: 7283

## Part 2

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

    abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b

This list represents answers from five groups:

- In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
- In the second group, there is no question to which everyone answered "yes".
- In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
- In the fourth group, everyone answered yes to only 1 question, a.
- In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

Answer: 3520

## Commentary / Approach to the Problem
### 2020 Original Solution
#### Part 1
In my original 2020 solution I did some convoluted work in my grouping function with sublists, although it was my introduction to the need for list.copy() if you are appending a list to another list. Otherwise, changing the sublist later will change what you’ve put into the list. [In reading the Kotlin solution on the Kotlin blog](https://blog.jetbrains.com/kotlin/2021/09/idiomatic-kotlin-set-operations/) I realize this is one of those situations where it would have been better to read the entire input into one string (not usually advisable in the real world) and then I could have split it up in one step. Alternatively, I could have done the looping and set insertion in one function and bypassed a lot of complications. We’ll see which method I go for when I solve this with other languages going forward.

#### Part 2
Once again, my 2020 solution was a bit more complicated than it needed to be. I could simply have looked for set intersections to get what I was looking for here. 

## What I Learned

### Generic

### Python

### Ruby

### Perl

