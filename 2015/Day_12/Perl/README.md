# What I learned about Perl on Day 12

## Part 1
- Nothing

## Part 2
- use Scalar::Util qw(looks_like_number) to figure out if something is a number
- using ref($scalar) eq "ARRAY" or ref($scalar) eq "HASH" to tell if they are hashes
- Apparently there's no way to tell if something is a string. If it's not a number, hash, or array - it's a string. So I ended up eliminating the string check that I had in Ruby and Python because it wasn't working well. 
- the same way that you can do (keys %hash), you can also do (values %hash)
- the JSON::PP library (which is built-in)
