#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DataFork, Junior Data Engineer, Question 2."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from question2 import solve


@mark.parametrize(
    "shops, visitors, ranges, ans",
    [(6, 5, [(3, 5), (2, 3), (4, 6), (1, 6), (5, 6)], {3, 4, 5}),
     (1, 1, [(1, 1)], {1}),
     param(1, 2, [(1, 1), (1, 2)], 1, marks=mark.xfail(reason='range(1, 2)'))]
)
def test_case1(shops, visitors, ranges, ans):
    """
    Test case from question2.py module docstring.

    Parameters
    ----------
    shops : int.
    visitors : int.
    ranges : List
        the range of visited shops (inclusive).
    ans : set
        expected answer.

    Returns
    -------
    None.

    """
    assert set(solve(shops, visitors, ranges)) == ans
