# Day 9: All in a Single Night

## Part 1

He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

- London to Dublin = 464
- London to Belfast = 518
- Dublin to Belfast = 141

The possible routes are therefore:

- Dublin -> London -> Belfast = 982
- London -> Dublin -> Belfast = 605
- London -> Belfast -> Dublin = 659
- Dublin -> Belfast -> London = 659
- Belfast -> Dublin -> London = 605
- Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

Answer: 117

## Part 2

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

Answer: 909 


## Commentary
As soon as I read this problem a lightbulb went off. This was so familiar. I remembered learning about this in undergrad, I think in my class called Discrete Algorithms. But I couldn't remember what it was called. A bit of Googling and I found out it was 
Dijkstra's algorithm. Now, could I find a site that could explain it in a way that I could understand again? (Because the wikipedia pseudocode didn't help.) Fortunately, my many Humble Bundle programming purchases had netted me the O'Reilly book _Algorithms in a Nutshell_ which had a couple implementation examples. I wasn't 100% sure how to implement at Graph in Python, but I had _Hands-On Data Structures and Algorithms with Python_. Turns out, when I re-read the problem, it's not really Dijkstra, because I don't have a specified destination. Instead, I think I need to either do Breadth or Depth first. Turns out this is actually a variant of the Traveling Salesman. Except in those, the salesman has to get back home. 


## What I learned from Each Language

### Python
- What a Hamilton Path is, what the Traveling Salesperson problem is (to be perfectly honest, I learned this in undergrad, but I couldn't remember ANYTHING about it). That the shortest Hamilton Path is a Traveling Salesman that never goes back home. To find it you create a fake city with 0 distance to all other cities.
- By the way, there is a Python package that will do this all for you: https://pypi.org/project/python-tsp/ you just need to supply it with a matrix

### Ruby
- Getting really familiar with Ruby has functions
- a really neat little function - if you have an array you have the method - each_with_index (eg array.each_with_index) and if used as part of a for loop can be like Python's enumerate. 
- [array.permutation method](https://www.rubydoc.info/stdlib/core/Array:permutation)
- the min and max methods on arrays

### Perl
