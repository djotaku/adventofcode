# What I learned from this day's problem

## Part 1
- I know I made things a bit more complicated than they needed to be with the search for abba and then passing all those to aaaa to make sure they weren't aaaa. I think a good refactor or way of looking at things in the other languages would be to combine those into one rule check.
- re.finditer to get all your matches. Had to use this instead of findall because I was using parenthesis to do duplicates and that makes findall not work intuitively for the entire match.
## Part 2
- using re.split to get everything that DOESN'T match the regex!