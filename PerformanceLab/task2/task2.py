from math import isclose, sqrt
from os import PathLike
from sys import argv
from typing import Sequence, Union


class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other) -> bool:
        other = Point.from_sequence(other)
        xcomp = isclose(self.x, other.x)
        ycomp = isclose(self.y, other.y)
        return xcomp and ycomp

    def __iter__(self) -> "Point":
        self.__counter = 0
        return self

    def __len__(self) -> int:
        return 2

    def __next__(self) -> float:
        if self.__counter == 0:
            self.__counter += 1
            return self.x
        elif self.__counter == 1:
            self.__counter += 1
            return self.y
        raise StopIteration

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        return str((self.x, self.y))

    @classmethod
    def from_file(cls, fpath: Union[str, PathLike]) -> "Point":
        with open(fpath, "r") as fl:
            return Point.from_string(fl.read())

    @classmethod
    def from_sequence(cls, pointlike: Union["Point", Sequence]) -> "Point":
        if isinstance(pointlike, Point):
            return pointlike
        return Point(pointlike[0], pointlike[1])

    @classmethod
    def from_string(cls, coords: str) -> "Point":
        x, y = (float(coord) for coord in coords.split())
        return Point(x, y)

    @property
    def dim(self) -> int:
        return len(self)

    def dist(self, other: "Point") -> float:
        other = Point.from_sequence(other)
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)


class Circle:
    def __init__(self, origin: Sequence, radius: float):
        self.origin = Point.from_sequence(origin)
        self.radius = float(radius)

    def __contains__(self, other: "Point") -> bool:
        return self.origin.dist(other) <= self.radius

    def __repr__(self) -> str:
        return f"Circle({repr(self.origin)}, {self.radius})"

    def __str__(self) -> str:
        return repr(self)

    @classmethod
    def from_file(cls, fpath: Union[str, PathLike]) -> "Circle":
        with open(fpath, "r") as fl:
            return Circle.from_string(fl.read())

    @classmethod
    def from_string(cls, coords: str) -> "Circle":
        origin, radius = (line.strip() for line in coords.split("\n"))
        return Circle(tuple(origin.split()), float(radius))


if __name__ == "__main__":
    if len(argv[1:3]) == 2:
        circle = Circle.from_file(argv[1])
        with open(argv[2]) as fl:
            for line in fl:
                point = Point.from_string(line)
                if point in circle:
                    if isclose(point.dist(circle.origin), circle.radius):
                        print(f"0 -> The {point} is on the {circle}")
                    else:
                        print(f"1 -> The {point} is inside the {circle}")
                else:
                    print(f"2 -> The {point} is outside the {circle}")
