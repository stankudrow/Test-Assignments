#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 1.
-----------

There are N water tankers with capacity Ci containing Wi amount of water.
The total amount of water is the sum of amount of the water in all the tankers.
The task is to transfer the total amount of water from one city to another.


Constraints
-----------

* 1 <= Ci <= 10e5

* 0 <= Wi <= Ci


Examples
--------

Capacities     : 4 9 6
Amount of water: 3 2 5
Output         : 2
Illustration   : {9: 9, 6: 1} or {9: 9, 4: 1} tankers with water.


Notes
-----
There was a condition on the number of tankers within [1; 10e5] integers.
"""


__author__ = "Stanislav D. Kudriavtsev"


from dataclasses import dataclass
from typing import List


@dataclass
class Tanker:
    """Tanker with capacity and amount of water in it."""
    capacity: float
    water: float

    def __post_init__(self):
        if not 1 <= self.capacity <= 10e5:
            raise ValueError("incorrect capacity")
        if not 0 <= self.water <= self.capacity:
            raise ValueError("incorrect water amount")


def solve(capacities: List, waters: List) -> int:
    """Solve the question 1. See this module docstring.

    Parameters
    ----------
    capacities : List
        the capacities of tankers.
    waters : List
        the amount of water in tankers.

    Returns
    -------
    int
        the minimum number of tankers to hold the total amount of water.

    """
    tankers: List = [Tanker(cap, wat) for cap, wat in zip(capacities, waters) if wat]
    tankers = sorted(tankers, key=lambda tanker: tanker.capacity)
    transfert: List = []
    while tankers:
        icur: int = 0  # current tanker index
        inxt = icur + 1
        leng: int = len(tankers)
        while (tankers[icur].capacity > tankers[icur].water) and (inxt < leng):
            water_to_get = tankers[icur].capacity - tankers[icur].water
            nxtwater = tankers[inxt].water
            water_to_take = (
                nxtwater if nxtwater <= water_to_get else nxtwater - water_to_get
            )
            if water_to_take:
                tankers[icur].water += water_to_take
                tankers[inxt].water -= water_to_take
            inxt += 1
        if tankers[icur].water:
            transfert.append(tankers[icur])
            tankers.pop(icur)
        tankers = [tanker for tanker in tankers if tanker.water]
    return len(transfert)


def main() -> int:
    """Entry point.

    Returns
    -------
    int
        The minimum number of tankers to transfer water.

    See Also
    --------
    solve
    """
    print("Please enter the capacities of tankers: C1 C2 C3 etc.")
    capacities = [int(cap) for cap in input().split()]
    print()
    print("Please enter the amount of water in tankers: W1 W2 W3 etc.")
    waters = [int(wat) for wat in input().split()]
    return solve(capacities, waters)


# if __name__ == '__main__':
#    print(main())
