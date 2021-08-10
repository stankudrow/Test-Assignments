#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 2.
-----------

There is a fair in a city that contains N shops.
The shops are arranged in a straight line at 1, 2, ..., N positions.
M persons come to the fair and each visits shops in the [L, R] inclusively.

Determine the three most popular shops.
The task is to fix the code, not to rewrite it.

Notes
-----
The code was rewritten, the input changed to accept data as for a single test.


Constraints
-----------

1st line: the number of shops: 1 <= N <= 10e5

2nd line: the number of vistors: 1 <= M <= 10e5

3d line:  the ranges of visited shops for each visitor:  1 <= L <= R <= N


Examples
--------

Input:

  1) 1 (one test case)

  2) 6 5 (N shops and M visitors)

  3-1) 3 5

  3-2) 2 3

  3-3) 4 6

  3-4) 1 6

  3-5) 5 6

Output:

  * 5 3 4

"""


__author__ = "Stanislav D. Kudriavtsev"


from operator import itemgetter
from typing import List, Tuple


# pylint: disable=unused-argument


def check_shops(shops: int):
    """Check if 1 <= shops <= 10e5."""
    if not 1 <= shops <= 10e5:
        raise ValueError("shops (={shops}) value is out of range")


def check_visitors(visitors: int):
    """Check if 1 <= visitors <= 10e5."""
    if not 1 <= visitors <= 10e5:
        raise ValueError("visitors (={visitors}) value is out of range")


def check_range(shops: int, left: int, right: int):
    """Check if the shop range is in 1 <= left <= right <= shops."""
    check_shops(shops)
    if not 1 <= left <= right <= shops:
        raise ValueError(f"range({left}, {right}) is invalid")


def check_bounds(shops: int, visitors: int, ranges: List[Tuple[int, int]]):
    """Check shops, visitors, ranges and if len(ranges) == visitors."""
    check_shops(shops)
    check_visitors(visitors)
    nrange = 0
    for left, right in ranges:
        check_range(shops, left, right)
        nrange += 1
    if nrange != visitors:
        raise ValueError("(len(ranges) = {nrange}) != (visitors = {visitors})")


def solve(shops: int, visitors: int, ranges: List[Tuple[int, int]]) -> List:
    """Select three most popular shops."""
    check_bounds(shops, visitors, ranges)
    shop_ranges = {}.fromkeys(range(1, shops + 1), 0)
    for _range in ranges:
        left, right = _range  # EAFP
        for shop in range(left, right + 1):
            shop_ranges[shop] += 1  # EAFP
    return sorted(shop_ranges, key=shop_ranges.get, reverse=True)[:3]


def main():
    """Entry point."""
    shops = int(input("The number of shops (N): "))
    check_shops(shops)
    visitors = int(input("The number of visitors (M): "))
    check_visitors(visitors)
    ranges = []
    for visitor in range(visitors):
        print(f"\nThe visitor {visitor} range:")
        left = int(input("L = "))
        right = int(input("R = "))
        check_range(shops, left, right)
        ranges.append((left, right))
    result = solve(shops, visitors, ranges)
    print(f'\nResult: {" ".join(map(str, result))}')


if __name__ == "__main__":
    main()
