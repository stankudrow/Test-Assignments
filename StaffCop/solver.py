#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""StaffCop Test Assignment."""


from typing import Callable, Dict

from point import Point


def sum_digits(num: int) -> int:
    """
    Sum the digits of the absolute value of an integer number.

    Parameters
    ----------
    num : int

    Returns
    -------
    int

    """
    return sum(map(int, str(abs(num))))  # in case of negative numbers


def check_point(weight: int) -> bool:
    """
    Check the point according to the distance weight.

    Parameters
    ----------
    point : Point

    Returns
    -------
    bool

    """

    def wrapper(point: Point):
        """Check if the sum of coordinates digits is <= the weight."""
        return sum(map(sum_digits, point.coords)) <= weight
    return wrapper


def solve(start: Point, func: Callable[[Point], bool]) -> Dict[Point, bool]:
    """
    Travel across the grid of 2D points from start while func is True.

    Parameters
    ----------
    start : Point
        starting point.
    func : Callable[[Point], bool]
        the conditioning function.

    Returns
    -------
    Dict[Point, bool]
        Point, status.

    """

    def move(point: Point) -> None:
        """Travel across the grid until it is possible."""
        if not points.get(point):
            flag = func(point)
            if flag:
                points[point] = True
                move(point + Point(0, 1))  # move upwards
                move(point + Point(1, 0))  # move rightwards

    points: Dict[Point, str] = {}
    start.dim = 2  # since non 2D point may be passed in
    move(start)
    return points


def main():
    """Entry point."""
    xcoord = int(input("int(x) = "))
    ycoord = int(input("int(y) = "))
    weight = int(input('int(weight) = '))
    points = solve(Point(xcoord, ycoord), check_point(weight))
    # print(f'\npoints = {points}\n')
    total = len(points)
    if total:
        total = 4 * total - 3  # avoid triple counting of original valid point
    print(f'total = {total}')


if __name__ == '__main__':
    main()
