# Day 6: Probably a Fire Hazard

## Part 1

You've decided to deploy one million lights in a 1000x1000 grid.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions you were sent in order.

For example:

- turn on 0,0 through 999,999 would turn on (or leave on) every light.
- toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
- turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

Answer: 377891

## Part 2

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

- turn on 0,0 through 0,0 would increase the total brightness by 1.
- toggle 0,0 through 999,999 would increase the total brightness by 2000000.

Answer: 

## Commentary
- After reading part one, my initial thought process is to create at least 3 methods:
	- find_rectangle - this would figure out which lights are involved
	- take_action - this would use xor to handle toggles, or 1 for on, and and 0 for off.
- What I'm not sure about is how to represent this. I feel like easiest is to just initialize a 2D matrix to 0s. I'm not sure dictionaries are the best idea here. Although, that would allow me to not have a real 2D matrix. I could just have the tuples be dictionary keys. Will have to think about this a bit.
- As you can see, I ended up going with a dictionary and it was pretty darn easy. XOR was definitely the right choice for switching. But it was easier to just set 1 or 0 for on and off.

