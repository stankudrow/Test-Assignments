#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 1 - Strictly increasing sequence.
------------------------------------------

Given an array consisting of N non-negative integers.
Check if a sequence may be a strictly (!) increasing one.

For an element A[i] of the array, 1 <= i <= N:
    * select a non-negative X number 0 <= X <= A[i]
    * reduce A[i] to A[i] - X

Print "Yes" if a sequence may be converted or "No" otherwise.


Constraints
-----------

* 1 <= T <= 10
* 1 <= N <= 1e5
* 0 <= A[i] <= 1e5


Example
--------

T:                  1
N:                  3
A:                  2 6 5
Expected result:    Yes

Initially an array is not a strictly ascending one.
However, 2 3 5 (X = 3) or 2 4 5 (X = 2) are.
Therefore, the sequence can be converted, so "Yes".
"""


__author__ = "Stanislav D. Kudriavtsev"

from typing import List


def solve(nels: int, arr: List[int]) -> bool:
    """Check if a sequence is convertable to a strictly increasing one.

    Parameters
    ----------
    nels: int - number of elements
    arr: Sequence - sequence to convert

    Returns
    -------
    bool
    """
    nels = len(arr)
    for i in range(nels - 2, -1, -1):
        if arr[i] >= arr[i + 1]:
            arr[i] = arr[i + 1] - 1
            if arr[i] < 0:
                return False
    return True


def main() -> None:
    """Entry point."""
    times = int(input("T = "))
    for _ in range(times):
        nels = int(input("N = "))
        arr = list(map(int, input("A = ").split()))
        out = solve(nels, arr)
        print("Yes" if out else "No")


if __name__ == "__main__":
    main()
