#!/usr/bin/env python3
"""Entry for the make.fun competition 'One Star for Monday'.

A one-star review of Monday written as if Monday were a restaurant:
the table was booked for two, the inbox got seated instead, the coffee
arrived cold, and Friday was not on the menu yet. The program writes
that single line to /output/entry.txt with no trailing newline.
"""

LINE = (
    "Booked a table for two at 7 a.m.; they seated my inbox instead, "
    "served the coffee cold, and Friday wasn't on the menu yet."
)


import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
