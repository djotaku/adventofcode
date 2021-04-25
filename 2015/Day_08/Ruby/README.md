# What I learned about Ruby from Day 08

## Part 1
- blocks in Ruby don't need something like pass, so I was just able to do ```if backspace_or_unicode == nil``` and keep going.
- ```string.delete_prefix``` and ```string.delete_suffix``` are the equivalent of lstrip and rstrip in Python
- Other than that, mostly just continuing with what I learned in previous days. 

## Part 2
- how to use string.count - you do string.count 'xyz' where x, y, and z (or more) are characters to look for and count. If you do (what was more intuitive to me) string.count 'x', 'y', 'z' then it looks for the intersection of those characters and you will not get the answer you expect.
