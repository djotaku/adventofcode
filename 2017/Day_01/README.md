# Day 01 - Inverse Captcha

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2017/day/1).

## Part 1
Answer: 1089

## Part 2
Answer: 1156

## Commentary / Approach to the Problem

### Part 1
Looks like I'll use the strategy I used for 2015 Day 05:

```python
double_letter = re.compile(r'(.)\1')
```

Then do a separate check to compare the first and last number.

### Part 2
I think for this part, it's probably better not to use regex. Just search within Python. 

## What I Learned

### Generic

### Python
- A new type of lookahead in order to allow for overlapping without using the regex module. re.compile(r'(\d)(?=\1)')

### Ruby
- A reminder that array.each_with_index is the equivalent to Python's enumerate(list)
### Perl

### Go (Golang)
- Go does not support lookaheads in regular expressions
- I continue to rue runes and how they are what you get from strings
### Haskell

### Rust
#### From my attempt
- if you have a str and want to get characters out of it, you can use .chars() it's like .iter, but beware that if you have UTF-8, you might not get what you expect.    
- collect allows you to transform one type of iterator into another
- because rust wants to be safe, if something like a type conversion might not work, to turn an Option<T> into T youneed you use unwrap_or()
- for some reason getting the last element of an array requires an unwrap (why might there not be a last element?)
#### from Reddit
Check out the code someone gave me to make my code more Rusty -> [here](https://github.com/djotaku/adventofcode/blob/849c1e8d7c096db03c98954244a54ff705febe77/2017/Day_01/Rust/reddit_solution.rs)

- The windows() method on an iterator to get sub iterators you can work on
- in that example, the chain method allows for getting the first and last number
- if you have ASCII characters you can subtract b'0' from the character to get the value in numbers. And if you're talking about ASCII digits, you can turn it into a number without all the rigamarole I'm going through with the to_digit(10) and the unwrap_or()
- just as in Ruby solutions if you're chaining methods you can chain a filter onto a map and get the transformation. In this case it's quite elegant how the person who helped me used the filter to avoid the if statement and the need to guard against going past the last index

also another snippet that is capable of doing both parts 1 and 2 (but not at once):

```rust
captcha
    .chars()
    .cycle()
    .skip(lookahead_index)
    .zip(captcha.chars())
    .filter_map(|(a, b)| (a == b).then_some(a.to_digit(10).unwrap()))
    .sum()
```

### Julia
    
