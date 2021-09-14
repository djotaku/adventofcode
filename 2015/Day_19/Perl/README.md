# What I learned about Perl on this day

## Part 1
- using substr to replace parts of a string - although tricky - you don't actually want the result you want the original string. This is why I had to have the variable $change_me to be changed so I could preserve the original molecule
- The existence of the $-[0] and $+[0] after you do a regex match. They return the start and end of a match, respectively. (I think + give you the index after the last character of the match)
- the Set::Scalar module. Previously I'd used Set::Object, but as I was just holding scalars this time (text) I figured I'd use this one. 
