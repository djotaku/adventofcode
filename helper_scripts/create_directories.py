import os
import shutil

HOME = os.getenv('HOME')
YEAR = 2016
PROGRAMMING_LANGUAGES = ["Python", "Ruby", "Perl", "Haskel", "Go"]


def create_advent_of_code_setup():
    for day in range(1, 26):
        os.mkdir(f"{HOME}/Programming Projects/adventofcode/Day_{day}")
        shutil.copyfile(f"{HOME}/Programming Projects/adventofcode/helper_scripts/daily_readme_template.md",
                        f"{HOME}/Programming Projects/adventofcode/Day_{day}/README.md")
        for programming_language in PROGRAMMING_LANGUAGES:
            os.mkdir(f"{HOME}/Programming Projects/adventofcode/Day_{day}/{programming_language}")
            shutil.copyfile(f"{HOME}/Programming Projects/adventofcode/helper_scripts/language_readme_template.md",
                            f"{HOME}/Programming Projects/adventofcode/Day_{day}/{programming_language}/README.md")


if __name__ == "__main__":
    create_advent_of_code_setup()
