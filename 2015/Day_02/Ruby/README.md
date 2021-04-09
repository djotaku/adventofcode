# What I learned in Ruby on Day 2

## Part 1

- Using .map(&:to_i) to change an entire array from string to int without having to explicitly loop thrhough the array. I'm not 100% sure on the & in there. Doing a bit more googling seems to suggest that the more likely way this would appear is:

```
array.map { |string| string.to_i}
```

