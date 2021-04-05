#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 test module."""


__author__ = "Stanislav D. Kudriavtsev"


import json
import pytest

from pathlib import Path
from task1 import get_task_data
from task1 import process_task


@pytest.fixture
def initial_data():
    """Return the initial cleaned data from task files."""
    return get_task_data()


def test_get_task_data(initial_data):
    """Test if all initial files are loaded and are indeed initial."""
    assert len(initial_data) == 4
    for key in ['error', 'struct', 'testcase', 'values']:
        fpath = Path() / 'files' / 'cleaned' / f'{key}.json'
        with open(fpath) as jf:
            assert initial_data[key] == json.load(jf)


def test_process_testcase(initial_data):
    """Test the case after procession with values."""
    testcase = initial_data['testcase']
    values = initial_data['values']
    result = process_task(testcase, values)
    respar = result['params']
    assert respar[0]['id'] == 34
    assert respar[0]['value'] == 298
    assert respar[1]['id'] == 146
    assert respar[1]['value'] == 'Валидация параметров на подаче объявления'
    assert respar[4]['id'] == 421
    assert respar[4]['value'] == 'High'
    assert respar[5]['id'] == 2128
    assert respar[5]['value'] == 'production'
    assert result == initial_data['struct']