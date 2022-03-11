#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 2 - Maximum Similarity.
--------------------------------

Two strings are given which can be shuffled.
Maximise the number of common possible positions.


Constraints
-----------
R and S are strings
* 1 <= T <= 10
* 1 <= [R], [S] <= 1e5
* Strings are supposed to be lowercase


Example
--------

T:                  1
R:                  bcda
S:                  ebac
Expected result:    3

Strings can be rearranged in a following way:
    abcd
    abce
Which have 3 common chars at corresponding indices.
"""

__author__ = "Stanislav D. Kudriavtsev"


def maximum(str1: str, str2: str) -> int:
    """Return the maximum common lengths of two strings."""
    return len(set(str1) & set(str2))


def main() -> None:
    """Entry point."""
    times = int(input("T = "))
    for _ in range(times):
        str1 = input()
        str2 = input()
        out = maximum(str1, str2)
        print(out)


if __name__ == "__main__":
    main()
