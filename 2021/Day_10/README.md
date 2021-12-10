# Day 10: Syntax Scoring

Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

Visit the version with all the story elements [here](https://adventofcode.com/2021/day/10).

## Part 1
The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

- If a chunk opens with (, it must close with ).
- If a chunk opens with [, it must close with ].
- If a chunk opens with {, it must close with }.
- If a chunk opens with <, it must close with >.

So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

    [({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]

Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

- {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
- [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
- [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
- [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
- <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

Stop at the first incorrect closing character on each corrupted line.

To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

- ): 3 points.
- ]: 57 points.
- }: 1197 points.
- >: 25137 points.

In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

Answer:

## Part 2

## Commentary / Approach to the Problem
### part 1
I think maybe make a dict where the key is the opening character (eg ([{ ) and the value is the closing character (eg )]}). Iterate over the characters on the line. If the char you find is in keys (meaning it’s an opening character), make that your new character for which you’re looking for a closer. If the char you find is not in keys, then you check if it’s your current character’s closer. If it is, go back to the previous one. (May need a list that we’re appending and popping because we may end up several layers deep). If not, it’s invalid. Have another dict that contains the values for errors. Append to a list that’s keeping track of score. Sum that and you have your answer.

## What I Learned

### Generic

### Python

### Ruby

### Perl

### Go (Golang)

### Haskell
    