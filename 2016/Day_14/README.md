# One-Time Pad

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2016/day/14).

## Part 1
To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:

- It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
- One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.
Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:

- The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
- The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
- None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999. 
- Eventually, index 22728 meets all of the criteria to generate the 64th key.
So, using our example salt of abc, index 22728 produces the 64th key.

Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?

Your puzzle input is ihaygndm

Answer: 15035
## Part 2
To implement key stretching, whenever you generate a hash, before you use it, you first find the MD5 hash of that hash, then the MD5 hash of that hash, and so on, a total of 2016 additional hashings. Always use lowercase hexadecimal representations of hashes.

For example, to find the stretched hash for index 0 and salt abc:

- Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.
- Then, find the MD5 hash of that hash: eec80a0c92dc8a0777c619d9bb51e910.
- Then, find the MD5 hash of that hash: 16062ce768787384c81fe17a7a60c7e3.
-  ...repeat many times...
- Then, find the MD5 hash of that hash: a107ff634856bb300138cac6568c0f24.
So, the stretched hash for index 0 in this situation is a107ff.... In the end, you find the original hash (one use of MD5), then find the hash-of-the-previous-hash 2016 times, for a total of 2017 uses of MD5.

The rest of the process remains the same, but now the keys are entirely different. Again for salt abc:

- The first triple (222, at index 5) has no matching 22222 in the next thousand hashes.
- The second triple (eee, at index 10) hash a matching eeeee at index 89, and so it is the first key.
- Eventually, index 22551 produces the 64th key (triple fff with matching fffff at index 22859.
Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key stretching, what index now produces your 64th one-time pad key?

Answer: 19968
## Commentary / Approach to the Problem
### Part 1
My plan was to generate and store one thousand hashes. After that, add a hash each time. This is not wasted computation because I eventually need to 
get to those hashes anyway to check them for triples. 

Keep a counter running so that you know when you get to the 64th one.

I am planning on using regex to search for triples and then quintuples.

I'm guessing that a potential gotcha is that an MD5 hash might have more than one triple and you have to check each of those for quintuples.  

At the very least this should benefit greatly from unit tests on the sample data (even if it doesn't present the gotchas.)

### Part 2
Went with the naive solution and it was fast enough - even in Python.

## What I Learned

### Generic

### Python
For Python, searching for a string with 
```python
'y' in 'xdfy'
```
is a seven times faster than the regex.
### Ruby

### Perl

### Go (Golang)

### Haskell
