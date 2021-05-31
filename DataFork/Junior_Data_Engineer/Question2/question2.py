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


Constraints
-----------

* 1 <= N <= 10

* 3 <= N, M <= 10e5

* 1 <= L <= R <= N


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

# According to the module docstring, the results of the example are:
#     shop : visited
#     1    : 1
#     2    : 2
#     3    : 3
#     4    : 3
#     5    : 4
#     6    : 3
# So the result of the solve function is not totally correct.

__author__ = "Stanislav D. Kudriavtsev"


# I could not help myself not to rewrite the code.


# pylint: disable=unused-argument
def solve(shops, visitors, shop_ranges):
    """Select three most popular shops."""
    # fix bugs in this function
    shops = {}.fromkeys(range(1, shops + 1), 0)
    for shrange in shop_ranges:
        left, right = shrange  # EAFP
        for shop in range(left, right + 1):
            shops[shop] += 1  # EAFP
    return sorted(shops, key=shops.get, reverse=True)[:3]


def main():
    """Entry point."""
    # a little refactoring here
    test_cases = int(input())
    for _ in range(test_cases):
        shops, visitors = map(int, input().split())
        shop_ranges = [tuple(map(int, input().split())) for _ in range(visitors)]
        result = solve(shops, visitors, shop_ranges)
        print(f'\nResult: {" ".join(map(str, result))}\n')
