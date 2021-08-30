#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Veeam Software Test Assignment 2: hash functions"""


import hashlib

from pathlib import Path
from typing import Union


PathType = Union[str, Path]


def hash_file(path: PathType, algo: str, enc: str = "utf-8", bsize: int = 65536) -> str:
    """
    Hash the name and contents of a file.

    Parameters
    ----------
    path : PathType
        file to hash.
    algo : str
        hash algorithm name supported by haslib Python module.
    enc : str, optional
        string encoding. The default is "utf-8".
    bsize : int, optional
        buffer/block size to read. The default is 65536.

    Returns
    -------
    str
        DESCRIPTION.

    """
    path = Path(path)
    with open(path, encoding=enc) as inf:
        hashalgo = getattr(hashlib, algo)()
        hashalgo.update(path.name.encode(enc))
        buffer = inf.read(bsize)
        while len(buffer) > 0:
            hashalgo.update(buffer.encode(enc))
            buffer = inf.read(bsize)
    return hashalgo.hexdigest()
