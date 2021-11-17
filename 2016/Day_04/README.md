# Day 4: Security Through Obscurity

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/4).

## Part 1
Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

- aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
- a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
- not-a-real-room-404[oarel] is a real room.
- totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

Answer: 245102
## Part 2
The room names are encrypted by a state-of-the-art [shift cipher](https://en.wikipedia.org/wiki/Caesar_cipher), which is nearly unbreakable without the right software.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

Answer: 324
## Commentary / Approach to the Problem
### Part 1
Seems like regex followed by similar technique as used in 2015 Day 5 with the rules in which you’re counting letters. (At least the Ruby solution there might help with the Ruby solution). There are some Python tools in itertools or somewhere that might help with the counting. Will also need to keep track of the sector IDs of the winners. Alphabetical check for ties may involve chr/ord (and similar functions in various languages) to make sure they’re in the proper order. This one is going to be relatively complex because there’s a lot to check per room in the directory.
### Part 2
I wasn't sure what to do because I assumed that Eric Wastl would make it obvious what I wanted to look for in the decrypted string. Apparently it wasn't and you were supposed to just look at some 300-odd output strings. Or at least that's what folks on the subreddit said. I still think that's not right, but I *was* able to get the right answer.
## What I Learned

### Generic

### Python
- all([]) is True (unintuitively!)
- using string.ascii_lowercase to get the alphabet!
### Ruby
- tally to count based on scan (giving a regex-like set to count)
- sort_by and how to sort by more than one attribute
### Perl

### Go (Golang)

### Haskell
