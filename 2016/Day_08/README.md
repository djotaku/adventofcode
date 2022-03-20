# Title of Problem

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/8).

## Part 1
The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

- rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

- rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

- rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

- rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

Answer: 119

## Part 2
You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

Answer: ZFHFSFOGPO


## Commentary / Approach to the Problem
It was pretty straightforward
## What I Learned

### Generic

### Python
- Nothing, but a reminder that to print without a newline, you need to do print("something", end='')'
### Ruby

### Perl

### Go (Golang)

### Haskell
