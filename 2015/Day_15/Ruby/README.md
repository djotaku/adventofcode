# What I learned about Ruby 

## Part 1
- How to do permutations in Ruby
- Permutations in Ruby are WAAAAAAAAAY slower than in Python. At least as of [this commit](https://github.com/djotaku/adventofcode/blob/697233772f48cae6118c453e79487a3a247db686/2015/Day_15/Ruby/part_1.rb)
- After getting some help from the folks in the Ruby subreddit, I redid things to the current commit.
- getting better at using map where I'd use list comprehensions in Python
- array.transpose - it takes a list of arrays [[1,2,3,4], [5,6,7,8]] and turns it into [[1,5], [2,6], [3,7], [4,8]] and I used that to multiply across categories
- Because the permutations were taking forever, I went to the ruby subreddit and got some awesome advice. Then user Godde, who was helping me, wanted to take a pass at the most idiomatic Ruby version he could make. Here's his explanation:

"I consider this idiomatic in that it uses the available features from the language (&:sum, :*, rest parameter) and standard library (flat_map, product, select, reduce, max, transpose) as much as possible instead of writing stuff out imperatively (e.g. manually finding the biggest value). This way the code reads almost as English and most people familiar with programming should be able to deduce how it functions even without knowing Ruby (except maybe for the lazy flat-mapped product workaround)."

```ruby
# [number, number, number, number, calories (number)][]
ingredients = File.readlines('input.txt')
                  .map { |line| line.match(/^.*: .* ([-\d]+), .* ([-\d]+), .* ([-\d]+), .* ([-\d]+), .* ([-\d]+)$/)[1..].map(&:to_i) }

spoon_counts = (0..100).to_a
puts spoon_counts.lazy
  .flat_map { |r| [r].product(*([spoon_counts] * (ingredients.size - 1))) } # Workaround for lazy Array#product
  .select { |counts| counts.sum == 100 }
  .map    { |counts| ingredients.zip(counts).map { |values, count| values.map { |v| v * count } }.transpose.map(&:sum) }
  .select { |*scores, calories| calories == 500 && scores.none?(&:negative?) }
  .map    { |*scores, _| scores.reduce(:*) }
  .max
```
And I had some questions about *scores and he added:

"|*scores, calories| means _put the last argument into calories and all the preceding arguments into an array called scores. Since the block is given an array, this is about equivalent to { |arguments| scores = arguments[...-1]; calories = arguments[-1]; ... }. In this case the whole array goes into arguments first. It's just an easier (and arguably more readable) way of doing that, though how Ruby handles passing array arguments to blocks might seem a little magical at first."