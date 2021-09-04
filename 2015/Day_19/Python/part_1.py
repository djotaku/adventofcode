import re


def generate_replacements(string_to_replace: str, replace_with_string: str, molecule: str):
    """Given a string to replace and a replacement string, replace each instance one by one.

    One by one constraint is why we can't just use Python's string.replace.
    """
    match = re.finditer(string_to_replace, molecule)
    print(match)
    for m in match:
        print(f"{m.start()}, {m.end()}, {m.group(0)}")


if __name__ == "__main__":
    generate_replacements("H", "HO", "HOOH")

