#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2 test module."""


__author__ = "Stanislav D. Kudriavtsev"


import pytest

try:
    import ujson as json
    #pass
except ImportError:
    import json  # type: ignore

from os.path import exists

from task2 import AM


def test_machine_creation1():
    """Test creation of an automatic machine."""
    assert AM()


def test_machine_creation2():
    """Test machine creation - no arguments needed."""
    with pytest.raises(TypeError):
        AM(10)


def test_machine_repr():
    """Test repr(machine)."""
    assert repr(AM()) == "AM()"


def test_machine_str():
    """Test str(machine)."""
    assert str(AM()) == repr(AM())


def test_has_validate_point():
    """Test hasattr(AM(), '_validate_point')."""
    assert hasattr(AM(), "_validate_point")


def test_validate_points_nonintegers():
    """Test non-integer values."""
    am = AM()
    gibberish = [[], (0,), {-1, 0, 1}, AM()]
    data = [-1.0, -0.9, 0.0, 0.1, 50.0, 99.9, 100.0, 100.1] + gibberish
    for dp in data:
        with pytest.raises(TypeError):
            AM._validate_point(dp)


def test_validate_points_negative_integers():
    """Test negative integers."""
    am = AM()
    data = [-100, -50, -1]
    for dp in data:
        with pytest.raises(ValueError):
            AM()._validate_point(dp)


def test_has_get_discount():
    """Test hasattr(AM(), 'get_discount')."""
    assert hasattr(AM(), "get_discount")


@pytest.fixture
def load_data():
    """Load test data from json file."""
    testfile_name = "test_task2_indata.json"
    assert exists(testfile_name)
    with open(testfile_name) as tf:
        data = {int(k): v for k, v in json.load(tf).items()}
    assert list(data) == [1, 3, 5, 10]
    return data


def test_discounts(load_data):
    """Test discounting scheme."""
    am = AM()
    for discount, points in load_data.items():
        discount /= 100
        for point in points:
            assert discount == am.get_discount(point)
