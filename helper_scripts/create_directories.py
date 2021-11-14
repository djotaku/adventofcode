import argparse
import os


HOME = os.getenv('HOME')
PROGRAMMING_LANGUAGES = ["Python", "Ruby", "Perl", "Haskell", "Go"]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", help="Year of Advent of Code")
    return parser.parse_args()


def create_language_readme_template(language: str, year: int, day: int):
    output_string = f"""# What I learned about {language} from this day's problem
    
    ## Part 1
    
    ## Part 2
    """
    with open(f"{HOME}/Programming Projects/adventofcode/{year}/Day_{day:02d}/{language}/README.md", "w") as file:
        file.write(output_string)


def create_daily_template(year: int, day: int):
    output_string = f"""
    
    # Title of Problem

    Out of respect for the author's wishes, I only put as much of the problem text as necessary to understand the problem.

    Visit the version with all the story elements [here](https://adventofcode.com/{year}/day/{day}).

    ## Part 1

    ## Part 2

    ## Commentary / Approach to the Problem

    ## What I Learned

    ### Generic

    ### Python

    ### Ruby

    ### Perl

    ### Go (Golang)

    ### Haskell
    """
    with open(f"{HOME}/Programming Projects/adventofcode/{year}/Day_{day:02d}/README.md", "w") as file:
        file.write(output_string)


def create_advent_of_code_setup(year: int):
    os.mkdir(f"{HOME}/Programming Projects/adventofcode/{year}")
    for day in range(1, 26):
        os.mkdir(f"{HOME}/Programming Projects/adventofcode/{year}/Day_{day:02d}")
        create_daily_template(year, day)
        for programming_language in PROGRAMMING_LANGUAGES:
            os.mkdir(f"{HOME}/Programming Projects/adventofcode/{year}/Day_{day:02d}/{programming_language}")
            create_language_readme_template(programming_language, year, day)


if __name__ == "__main__":
    args = parse_args()
    the_year = args.year
    create_advent_of_code_setup(the_year)
