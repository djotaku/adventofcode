[Cute Version](https://adventofcode.com/2020/day/11)

# Part 1

For example, the initial seat layout might look like this:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL
   

- If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
- If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
- Otherwise, the seat's state does not change.

Eventually the chaos stabilizes and further applications of these rules cause no seats to change state!

Applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

# Part 2

instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions

