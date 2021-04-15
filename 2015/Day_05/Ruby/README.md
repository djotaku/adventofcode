# What I learned in Ruby on Day 05

## Part 1
- An equivalent to the Python findall() with regular expressions is to use .scan on a string with an RE expression as the params. Then use a for loop to collect the number of times it matches.
- Many, MANY thanks to the folks who helped me on the [ruby subreddit](https://www.reddit.com/r/ruby/), especially [here](https://www.reddit.com/r/ruby/comments/mrkjgi/xpost_is_there_a_way_to_represent_rule_2_in/) where I learned:
	- if I want to force a bool, I could return !! expression or I could use .match? <- adding the question mark
	- Or should use assert instead of assert_equal(true, exp)
	- AND getting #<MatchData "aa" 1:"a"> was not an error, but the unit test telling me I'd succeeded
- something
