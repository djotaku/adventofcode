# Day 02 - I Was Told There Would Be No Math

To read the story-version at AoC go [here](https://adventofcode.com/2015/day/2)

## Part 1

find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. They also need a little extra paper for each box: the area of the smallest side.

For example:

- A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
- A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the list are in feet. How many total square feet of wrapping paper should they order?

Answer: 1598415


## Part 2

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present.

For example:

- A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
- A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?

Answer: 3812909

## What I learned Roundup

### Python

- It's my first time using reduce. I thought I wanted to use accumulate, but that returns an iterator. Since I just wanted to add things up reduce was just fine. Also my first time writing a lamba function. Woohoo!

### Ruby

- Using .map(&:to_i) to change an entire array from string to int without having to explicitly loop through the array. I'm not 100% sure on the & in there. Doing a bit more googling seems to suggest that the more likely way this would appear is:

```
array.map { |string| string.to_i}
```

- Used reduce. Although I used to hate lambdas, I actually kind of like the lamba syntax in Python a little more. Because sum seems to be an extra variable - at least the way I see it. 

- How do to Ruby's equivalent to Python's 

```
if __name__=="__main__":
```
without that, very hard to do unit testing. The answer is:

```
if $PROGRAM_NAME == __FILE__
  foo()
  bar()
end 
```
### Perl

- how to use regular expressions instead of split to get my puzzle input (see part_1.pl line 13)
- sorting numerically is a lot more complicated in Perl than the other languages (see part_1.pl line 17)
- Perl doesn't have reduce in the standard library
- push is used to add to arrays