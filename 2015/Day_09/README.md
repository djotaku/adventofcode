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
- how to create a subroutine
- how to pass an arrays and hashes to a subroutine
    - I have to say that this is the most frustrating system between Perl, Python, and Ruby for passing items in. It really is annoying to figure out what is the right thing to do to accurately grab from the @_ or $_ or even if you should be using one or the other. Guess I'm going to learn over the next few problem sets. Yeesh! (The day after I wrote this, I went over the chapter in Programming Perl that explains it a little better. I think I have it now.)
    - while using subroutines in Perl forced me to wrap my head around the weird way Perl thinks with passing in arrays and hashes, I did like how much easier it was to make my hash of hashes than it was in Python (or Ruby) where I had to first check if it was in the dict (or hash). 
- constantly changing the symbol from @ or % to $ is annoying
- ```my %index_dictionary = %city_dict_keys[0..$#city_dict_keys];``` aka Perl slices - requires v5.20
- Permutations (and, by extension, generators) in Perl
- Note to self: Requires toolbox as it makes use of an installed CPAN module [Algorithm::Permute](https://metacpan.org/pod/Algorithm::Permute)
- use List::Util qw(min); and qw(max)
