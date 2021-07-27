#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veeam Software Test Assignment 2.

Module with hash function(s).
"""


import hashlib

from pathlib import Path
from typing import Union


PathType = Union[str, Path]


def hash_file(path: PathType, algo: str, enc: str = "utf-8", bsize: int = 65536) -> str:
    """
    Hash the name and contents of a file.

    Parameters
    ----------
    path : Union[str, Path]
    algo : str
        hash algorithm from PyStd hashlib library.
    encoding : str, optional
        encoding before hashing. The default is 'utf-8'.
    bsize : int, optional
        buffer/block size. The default is 65536.

    Raises
    ------
    FileNotFoundError
        filepath does not exist or not a file.

    Returns
    -------
    str

    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    algo = getattr(hashlib, algo)()
    algo.update(path.name.encode(enc))
    with open(path, encoding=enc) as inf:
        buffer = inf.read(bsize)
        while len(buffer) > 0:
            algo.update(buffer.encode(enc))
            buffer = inf.read(bsize)
    return algo.hexdigest()
