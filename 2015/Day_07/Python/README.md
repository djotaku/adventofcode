# What I learned in Python on Day 07

## Part 1
- need to learn how to make Python just use a ushort so that it stays in the right range. Unfortunately my Python was compiled w/o the ability to use ctypes. Fortunately after trying different Google search terms for 2 days, I found that the answer is instead of using "~" to XOR it with 65535.
- You almost certainly want to be consistent with your return types. It seems I was getting an error with my break_up_equation function because in the case of a straight through eg lx -> b I wasn't returning it as a list-type or some kind of iterable, so it was making the if/else on the find_value_on_line no go all the way through.