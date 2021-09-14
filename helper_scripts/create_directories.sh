#!/bin/bash

# right now this doesn't do what it's supposed to. Just a placeholder

for num in {01..25}

do
mkdir "$HOME/Programming Projects/adventofcode/2016/Day_$num"
cp "$HOME/Programming Projects/adventofcode/helper_scripts/daily_readme_template.md" "$HOME/Programming Projects/adventofcode/2016/Day_$num/README.md"
git add "$HOME/Programming Projects/adventofcode/2016/Day_$num/README.md"
mkdir "$HOME/Programming Projects/adventofcode/2016/Day_$num/Python"
cp "$HOME/Programming Projects/adventofcode/helper_scripts/language_readme_template.md" "$HOME/Programming Projects/adventofcode/2016/Day_$num/Python/README.md"
mkdir "$HOME/Programming Projects/adventofcode/2016/Day_$num/Ruby"
cp "$HOME/Programming Projects/adventofcode/helper_scripts/language_readme_template.md" "$HOME/Programming Projects/adventofcode/2016/Day_$num/Ruby/README.md"

done 
