# What I learned in Ruby on Day 05

## Part 1
- An equivalent to the Python findall() with regular expressions is to use .scan on a string with an RE expression as the params. Then use a for loop to collect the number of times it matches.
- Many, MANY thanks to the folks who helped me on the [ruby subreddit](https://www.reddit.com/r/ruby/), especially [here](https://www.reddit.com/r/ruby/comments/mrkjgi/xpost_is_there_a_way_to_represent_rule_2_in/) where I learned:
	- if I want to force a bool, I could return !! expression or I could use .match? <- adding the question mark
	- Or should use assert instead of assert_equal(true, exp)
	- AND getting #<MatchData "aa" 1:"a"> was not an error, but the unit test telling me I'd succeeded
        - a few days later, user 442401 showed me a more Ruby-ish way to do Rules 1 and 2. You can see that [here](https://github.com/djotaku/adventofcode/blob/main/2015/Day_05/Ruby/part_1_more_rubyish.rb). He also had a great explanation of how the Rule 2 mod works:
        
        ```ruby
        string.chars                # returns an Array of characters, ['f', 'o', 'o', 'b', 'a', 'r']
        .each_cons(2)               # returns an enumerator for each array of consecutive 2 elements
                                    # [['f', 'o'], ['o', 'o'], ['o', 'b'] ....]
        .any? { |a, b| a == b }     # passes each pair into the block
                                    # which are allocated to variables a & b. and
                                    # returns true as soon the block evaluates to true.
                                    # The block (a == b) evaluates to true if the pair
                                    # contains equal elements and will return true for
                                    # the second pair ['o', 'o']
        ```
        
        
## Part 2
- very annoying that it doesn't have findall(), but turned out not to eventually be necessary.
