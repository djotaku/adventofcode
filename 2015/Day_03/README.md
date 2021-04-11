# Day 3: Perfectly Spherical Houses in a Vacuum

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2015/day/3).

## Part 1

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

- ">" delivers presents to 2 houses: one at the starting location, and one to the east.
- "^>v<" delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
- "^v^v^v^v^v" delivers a bunch of presents to some very lucky children at only 2 houses.

Answer: 2572

## Part 2

This time there is Santa and Robo-Santa who each take turns interpreting the directions.

This year, how many houses receive at least one present?

For example:

- "^v" delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
- "^>v<" now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
- "^v^v^v^v^v" now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

Answer: 2631


## Commentary
- Engineering joke in the title there. LOVE! IT!
- This is the first one where I have to do more than a little thinking to figure things out.
    - Initial thought is to create a Dictionary (or Hash in the non-Pythonic languages) with the coordinates as keys. Then put 1 into each key. This will auto-handle stopping at the same house twice. I think I might also be able to use ... Counter or some other such Python package to just sum these up rather than using a dictionary that I need to loop over. 
    - On second thought, I think I'm overthinking this. At least in Python I can use sets.

## What I Learned

### Python

Nothing new on this day

### Ruby

- For separating a string I like that split works in Ruby. Had to do a for loop in Python.
- For Ruby [need an import to use sets](https://ruby-doc.org/stdlib-2.7.1/libdoc/set/rdoc/Set.html).
- Ruby can have lists in Sets. Python requires them to be immutables.
- I tried to use a similar notation to what I learned about in the alternate Day 1 solution using reduce to recreate a kind of enumerate in Ruby and that didn't work. In the future I'll search and see if there's an enumerate function in the standard library.

### Perl

- Perl does not have sets built in. 
- using CPAN. Ended up using my toolbox container and installing cpan App::cpanminus as per the cpan documentation
- Perl doesn't appear to have tuples so, but the sets didn't need them. Just ended up adding in the coordinates as strings - at least that's what I believe Perl was doing under the hood. I got the right answer.