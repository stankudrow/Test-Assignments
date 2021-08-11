#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""StaffCop Test Assignment."""


from functools import total_ordering
from numbers import Real  # ???? mypy !!!!!
from typing import Iterable, List, Optional, Tuple


# The sympy package contains Point2D class.
# Here the Point2D is "remade" for an illustrative purpose.


# pylint: disable=line-too-long
# pydocstyle: ignore=D105


@total_ordering
class Point:
    """A point in n-dimentional euclidian space."""

    __slots__ = ("_coords", "_dim")

    @classmethod
    def from_iterable(
        cls, iterable: Iterable[Real], dim: Optional[int] = None
    ) -> "Point":
        """
        Create a point from iterable.

        Parameters
        ----------
        cls : Point
        iterable : Iterable[Real]

        Returns
        -------
        point : Point

        """
        return Point(*iterable, dim=dim)

    def __init__(self, *args: Tuple[Real, ...], dim: Optional[int] = None):
        self.coords = args
        if dim is not None:
            self.dim = dim

    def __add__(self, other):
        new_coords = [sitem + oitem for sitem, oitem in zip(self, other)]
        return self.from_iterable(new_coords)

    def __radd__(self, other):
        return self + other

    def __eq__(self, other):
        return self.coords == other

    def __hash__(self) -> int:
        return hash(tuple(self.coords))

    def __iter__(self):
        for coord in self.coords:
            yield coord

    def __lt__(self, other):
        return self.coords < other

    def __mul__(self, factor: Real):
        if not isinstance(factor, Real):
            raise TypeError("factor must be a real number")
        new_coords = [sitem * factor for sitem in self]
        return self.from_iterable(new_coords)

    def __neg__(self):
        return -1 * self

    def __rmul__(self, factor: Real):
        return self * factor

    def __repr__(self) -> str:
        return f'Point{repr(tuple(self.coords))}'

    def __str__(self) -> str:
        return repr(self)

    def __sub__(self, other):
        return self + (-other)  # __neg__

    @property
    def coords(self) -> List[Real]:
        """
        Return the coordinates of the point.

        Returns
        -------
        List[Real]

        """
        return self._coords

    @coords.setter
    def coords(self, iterable: Iterable[Real]):
        coords = []  # in case of generator/iterator passed in
        idim = 0
        for idim, item in enumerate(iterable, 1):
            if not isinstance(item, Real):
                raise TypeError(f"iterable[{idim}] == {item} is not of Real type")
            coords.append(item)
        self._coords = coords[:idim]
        self._dim = idim

    @property
    def dim(self) -> int:
        """
        Return the dimention of the point.

        Returns
        -------
        int

        """
        return self._dim

    @dim.setter
    def dim(self, ndim: int):
        if not isinstance(ndim, int):
            raise TypeError("the dimention must be an integer")
        if ndim < 0:
            raise TypeError("the dimention must be a non-negative integer")
        self._dim = ndim
        if getattr(self, "coords", False):
            re_coords = list(self.coords[:ndim])
            addend = [0 for _ in range(ndim - len(self.coords))]
            self.coords = re_coords + addend
        else:
            self.coords = (0 for _ in range(ndim))
