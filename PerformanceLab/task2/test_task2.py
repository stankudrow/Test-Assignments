from math import cos, isclose, radians as rads, sin, sqrt
from os import sep
from pytest import (
    mark,
    param,
)

from .task2 import Circle, Point


class TestPoint:
    @mark.parametrize(
        "x, y",
        [
            (-2.4, 0.8),
            (3, -1),
            param("a", 5, marks=mark.xfail(reason="str")),
            param([0], 5, marks=mark.xfail(reason="list")),
            param(-2, None, marks=mark.xfail(reason="None")),
        ],
    )
    def test_point_init(self, x, y):
        point = Point(x, y)
        assert point and point.x == x and point.y == y

    def test_length_and_dim(self):
        point = Point(0, 0)
        assert len(point) == point.dim == 2

    def test_iteration(self):
        coords = (-2, 4)
        point = Point(*coords)
        for tcoord, pcoord in zip(coords, point):
            assert tcoord == pcoord

    def test_repr_str(self):
        point = Point(-2, 2)
        assert repr(point) == f"Point({point.x}, {point.y})"
        assert str(point) == str((point.x, point.y))

    @mark.parametrize(
        "point1, point2, expected",
        [
            (Point(1, 1), Point(1, 1), True),
            (Point(0, 0), Point(3, 3), False),
        ],
    )
    def test_equality(self, point1, point2, expected):
        assert (point1 == point2) == expected

    @mark.parametrize(
        "string",
        [
            "  0   0  ",
            "	-4.7	-9.1\n",
        ],
    )
    def test_from_str(self, string):
        coords = string.split()
        assert Point.from_string(string) == Point(*coords)

    @mark.parametrize(
        "fname",
        [
            "good_file.txt",
            param("bad_file_invalid_data.txt", marks=mark.xfail),
        ],
    )
    def test_from_file(self, fname):
        fpath = sep.join(["assets", fname])
        with open(fpath) as fl:
            point = Point.from_string(fl.read())
            assert Point.from_file(fpath) == point

    @mark.parametrize(
        "point1, point2, expected",
        [
            (Point(0, 0), Point(2, 0), 2),
            (Point(0, 0), Point(1, 1), sqrt(2)),
            (Point(0, 2), Point(0, -3), 5),
        ],
    )
    def test_dist(self, point1, point2, expected):
        dst1 = point1.dist(point2)
        dst2 = point2.dist(point1)
        assert isclose(dst1, dst2)
        assert isclose(dst1, expected) and isclose(dst2, expected)


# The __init__ and __contains__ logic are of great interest
class TestCircle:
    @mark.parametrize(
        "pointlike, radius",
        [
            (Point(1, 1), 1),
            ((1, 1), 1),
            ((2, 1), 0),
        ],
    )
    def test_circle_init(self, pointlike, radius):
        circle = Circle(pointlike, radius)
        assert circle
        assert isclose(circle.radius, radius)
        assert tuple(circle.origin) == tuple(pointlike)

    @mark.parametrize(
        "circle, point, expected",
        [
            (Circle([0, 0], 0), Point(0, 0), True),
            (Circle([0, 0], 1), Point(0, 0.5), True),
            (Circle([0, 0], 1), Point(0.5, 0), True),
            (Circle([0, 0], 1), Point(1, 1), False),
            (Circle([0, 0], 1), Point(cos(rads(30)), sin(rads(30))), True),
            (Circle([0, 0], 1), Point(cos(rads(200)), sin(rads(200))), True),
        ],
    )
    def test_contains(self, circle, point, expected):
        assert (point in circle) == expected

    @mark.parametrize(
        "fname",
        [
            "file1_circle.txt",
        ],
    )
    def test_from_file(self, fname):
        fpath = sep.join(["assets", fname])
        with open(fpath) as fl:
            circle = Circle.from_file(fpath)
            origin, radius = fl.readlines()
            assert circle.origin == Point.from_string(origin)
            assert circle.radius == float(radius.strip())
