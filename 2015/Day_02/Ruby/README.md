# What I learned in Ruby on Day 2

## Part 1

- Using .map(&:to_i) to change an entire array from string to int without having to explicitly loop through the array. I'm not 100% sure on the & in there. Doing a bit more googling seems to suggest that the more likely way this would appear is:

```
array.map { |string| string.to_i}
```

- Used reduce. Although I used to hate lambdas, I actually kind of like the lamba syntax in Python a little more. Because sum seems to be an extra variable - at least the way I see it. 

## Part 2

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
