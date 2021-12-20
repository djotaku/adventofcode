# Day 20: Trench Map

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/20).

## Part 1
The first section is the image enhancement algorithm. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).

The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the image enhancement algorithm string.

Starting from the top-left and reading across each row...by turning dark pixels (.) into 0 and light pixels (#) into 1, the binary number 000100010 can be formed, which is 34 in decimal.

the character at index 34 can be found: #. So, the output pixel in the center of the output image should be #, a light pixel.

This process can then be repeated to calculate every pixel of the output image.

Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (.).

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?

Answer: 

## Part 2

## Commentary / Approach to the Problem
### Part 1
This seems to be our Game of Life problem (or one of them) for this year, so I'm going to treat it that way. I'm GUESSING that the point of the infinite field that Wastl keeps harping on means that pixels at the edge of our initial image will result in some pixels out beyond the initial borders.

Overall it hasn't been too hard. What's the hardest has been figuring out my boundaries for checking since it goes infinitely. Apparently because of the way he wrote it, the background flickers. I think the way to model this is to see how my current boundary changes as well as the points that are 1 outside of it. But for the next iteration I need to simulate a band of #s beyond that. Question is whether the band is 1 or 2 levels thick.

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
