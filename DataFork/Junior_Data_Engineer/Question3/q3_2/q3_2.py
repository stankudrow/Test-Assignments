#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 3 - Largest Rectangle.
-------------------------------

Given two arrays A and B of lengths N and M.
Consider the following (N = M) points on the coordinate plane:
    * [(a_1, 0), (a_2, 0), ..., (a_n, 0)]
    * [(b_1, 1), (b_2, 1), ..., (b_m, 1)]
Find the area of a largest rectangle.
If there is no rectangel, print 0.

Constraints
-----------

* 1 <= T <= 50
* 1 <= N, M <= 1e5
* 1 <= A, B <= 1e9


Example
--------

T:                  1
N M:                3 3
A:                  1 2 4
B:                  1 3 4
Expected result:    3

A [(1, 0), (1, 1), (4, 0), (4, 1)] rectangle can be constructed.
"""

__author__ = "Stanislav D. Kudriavtsev"

from typing import List


def largest_rectangle(npts: int, mpts: int, ptsn: List, ptsm: List):
    """Get the area of a largest rectangle."""
    # a dummy logic to silence linters
    npts, mpts = map(len, (ptsn, ptsm))
    if (npts > 1) and (mpts > 1):
        common = sorted(set(ptsn) & set(ptsm))
        if len(common) >= 2:
            return common[-1] - common[0]
    return 0


def main() -> None:
    """Entry point."""
    times = int(input("T = "))
    for _ in range(times):
        npts, mpts = map(int, input("N, M = ").split())
        ptsn = list(map(int, input("0: ").split()))
        ptsm = list(map(int, input("1: ").split()))
        out = largest_rectangle(npts, mpts, ptsn, ptsm)
        print(out)


if __name__ == "__main__":
    main()
