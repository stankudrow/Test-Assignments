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

    def move(start: Point, dx: Point, dy: Point) -> int:
        """Travel across the grid until it is possible."""

        def travel(point: Point, dx: Point, dy: Point) -> None:
            """Travel across the quadrant by moving towards dx and dy."""
            is_visited: Optional[bool] = vpoints.get(point)
            if is_visited is None:
                status = func(point)
                vpoints[point] = status
                if status:
                    travel(point + dx, dx, dy)
                    travel(point + dy, dx, dy)

        vpoints: Dict[Point, str] = {}  # visited points
        travel(start, dx, dy)
        vpoints = {pnt: stat for pnt, stat in vpoints.items() if stat}
        print(f'points:\n{vpoints}')
        return len(vpoints)

    start.dim = 2  # since non 2D point may be passed in
    total = 0
    total += move(start, Point(1, 0), Point(0, 1))                  # UR
    total += move(start - Point(0, 1), Point(1, 0), -Point(0, 1))   # RD
    total += move(start - Point(1, 0), -Point(0, 1), -Point(1, 0))  # DL
    total += move(start + Point(-1, 1), Point(0, 1), -Point(1, 0))  # UL
    return total
    #return {point: status for point, status in points.items() if status}


def main():
    """Entry point."""
    xcoord = int(input("int(x) = "))
    ycoord = int(input("int(y) = "))
    weight = int(input('int(w) = '))  # distance weight, see check_weight
    start = Point(xcoord, ycoord)
    print(f'\nstart = {start}')
    total = solve(start, check_point(weight))
    print(f'total = {total}')


if __name__ == '__main__':
    main()
