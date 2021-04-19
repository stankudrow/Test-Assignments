#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""AM - Automatic Machine calculating discounts."""


__author__ = "Stanislav D. Kudriavtsev"


class AM:
    """Automatic machine calculating discounts.

    The points are assumed to be nonnegative integers.

    The scheme of discounting:

      * from 0 (inclusive) to 100 (exclusive) - 1%;

      * from 100 to 200 - 3%;

      * from 200 to 500 - 5%;

      * from 500 - 10%;
    """

    def __repr__(self):
        return "AM()"

    def __str__(self):
        return repr(self)

    def _validate_point(self, point: int):
        """Check if the point is a nonnegative integer."""
        if not isinstance(point, int):
            raise TypeError(f"points must be integers")
        if point < 0:
            raise ValueError("points must be nonnegative integers")

    def get_discount(self, points: int):
        """Calculate a discount based on points."""
        self._validate_point(points)
        if 0 <= points < 100:
            return 0.01
        elif 100 <= points < 200:
            return 0.03
        elif 200 <= points < 500:
            return 0.05
        else:
            return 0.1


if __name__ == "__main__":
    am = AM()
    print(am)
