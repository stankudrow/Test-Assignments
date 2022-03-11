#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DataFork, Junior Data Engineer, Question 1."""


__author__ = "Stanislav D. Kudriavtsev"


from pytest import mark, param

from question1 import solve


@mark.parametrize("cap, wat, res", [([], [], 0), ([2], [], 0), ([], [2], 0)])
def test_empties(cap, wat, res):
    """
    Test (capacity, water) for an empty tanker.

    Parameters
    ----------
    cap : TYPE
        tanker capacity.
    wat : TYPE
        amount of water in a tanker.
    res : TYPE
        the minimum number of tankers to transfer the total amount of water.

    Returns
    -------
    None.

    """
    assert solve(cap, wat) == res


@mark.parametrize(
    "cap, wat, res",
    [
        param([5], [-1], 0, marks=mark.xfail),
        ([5], [0], 0),
        ([5], [1], 1),
        ([5], [5], 1),
        param([0], [6], 0, marks=mark.xfail),
        param([5], [6], 1, marks=mark.xfail),
    ],
)
def test_singles(cap, wat, res):
    """
    Test (capacity, water) for a single tanker.

    Parameters
    ----------
    cap : TYPE
        tanker capacity.
    wat : TYPE
        amount of water in a tanker.
    res : TYPE
        the minimum number of tankers to transfer the total amount of water.

    Returns
    -------
    None.

    """
    assert solve(cap, wat) == res


@mark.parametrize(
    "cap, wat, res",
    [([1, 2], [0], 0), ([1, 3], [1], 1), ([5], [0, 2], 0), ([4], [4, 1], 1)],
)
def test_unequal_capacity_water_amounts(cap, wat, res):
    """
    Test input data of unequal lenghts.

    Parameters
    ----------
    cap : TYPE
        tanker capacity.
    wat : TYPE
        amount of water in a tanker.
    res : TYPE
        the minimum number of tankers to transfer the total amount of water.

    Returns
    -------
    None.

    """
    assert solve(cap, wat) == res


@mark.parametrize(
    "cap, wat, res",
    [
        ([3, 3, 3], [1, 1, 0], 1),
        ([3, 3, 3], [1, 1, 1], 1),
        ([3, 3, 3], [1, 1, 2], 2),
        ([3, 3, 3], [3, 2, 0], 2),
        ([3, 3, 3], [3, 3, 0], 2),
        ([3, 3, 3], [3, 3, 1], 3),
        ([3, 3, 3], [3, 3, 3], 3),
        param([3, 3, 3], [3, 3, 4], 3, marks=mark.xfail),
    ],
)
def test_different_capwater_combinations(cap, wat, res):
    """
    Some of capicities-waters combinations.

    Parameters
    ----------
    cap : TYPE
        tanker capacity.
    wat : TYPE
        amount of water in a tanker.
    res : TYPE
        the minimum number of tankers to transfer the total amount of water.

    Returns
    -------
    None.

    """
    assert solve(cap, wat) == res
