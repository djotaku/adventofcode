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

Another really awesome solution from the subreddit (this time by mjgiarlo):

```ruby

# frozen_string_literal: true

TEASPOONS_MAX = 100

def ingredient_score(multipliers, cookies)
  final_score = 1
  property_count = 1 
  multipliers 
    .zip(cookies) 
    .map { |multiplication_item| multiplication_item.last.map { |x| multiplication_item.first * x } } 
    .transpose 
    .each do |cookie_property| 
      final_score *= cookie_property.sum if cookie_property.sum.positive?
      property_count += 1 
      return final_score if property_count == 5 
    end 
 end

def brute_force_cookie_score(ingredient_list)
  (1..TEASPOONS_MAX) 
    .to_a 
    .permutation(ingredient_list.length) 
    .filter_map { |combo| ingredient_score(combo, ingredient_list) if combo.sum == TEASPOONS_MAX } 
    .max
end

def parse_ingredients(path) 
  File.new(path).map do |line| 
    line 
      .match(/.+: capacity ([\d-]+), durability ([\d-]+), flavor ([\d-]+), texture ([\d-]+), calories ([\d-]+)/) 
      .captures 
      .map(&:to_i) 
  end 
end

if $PROGRAM_NAME == FILE 
  ingredients = parse_ingredients('../input.txt') 
  cookie_score = brute_force_cookie_score(ingredients) 
  puts "The cookie score is #{cookie_score}" 
end

```

## Part 2
- .select is faster than .map.compact
