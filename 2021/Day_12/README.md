# Day 12: Passage Pathing

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/12).

## Part 1

Answer: 5874
## Part 2

## Commentary / Approach to the Problem
### Part 1
At first I was happy because I thought it was going to be a traveling salesman problem. I created an algorithm for that with the 2015 problem set. But this is different as we're allowed to revisit some locations and not others.

Before trying to take the input and massage it into a graph, I wanted to see if I could start with a graph and use that to get to the same solution as the problem. This would allow me to see if the graph method would work before spending too much time with parsing.

Thinking through my algorithm:
- How do we know when to end? When have we exhausted all possibilities?
- Obviously we want a set to store possibilities to negate duplicates
- Need to be able to throw away paths that cannot finish because they'd require going through a lowercase twice
- Do we need a tree or other recursive way of exploring every possible intersection? Or do we relay on randomness and enough turns to get it right? If so, do we split into multiple functions?

After struggling on [this implementation](https://github.com/djotaku/adventofcode/blob/25bbbea180b80fc0b16e170e9108179e918b6577/2021/Day_12/Python/scrapped_solution.py) for a couple of hours, I decided to look up a DFS algorith and see if I could use that as a starting point.

So if a normal DFS looks like this:

```python
# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')
```
What I want is one there only small caves are added to the visited list. I also want it to end when we get to "end".

I got to [here](https://github.com/djotaku/adventofcode/blob/25bbbea180b80fc0b16e170e9108179e918b6577/2021/Day_12/Python/solution.py) and was struggling on how to set up the recursion. So I went to the megathreads to see what I was doing wrong.

[This one](https://www.reddit.com/r/adventofcode/comments/rehj2r/comment/hoabzvk/?utm_source=share&utm_medium=web2x&context=3) seemed to be very close to what I was already doing so I decided to adapt it to my solution.

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
