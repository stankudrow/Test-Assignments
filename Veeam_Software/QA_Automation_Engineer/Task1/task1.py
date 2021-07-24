#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Veeam Software Test Assignment 1."""


import xml.etree.ElementTree as ET

from pathlib import Path
from shutil import copy
from typing import List, Tuple


def parse_config_file(config_file: str) -> List[Tuple[Path, Path]]:
    """
    Parse XML config file with data for copying files.

    The file contains <file> tags with attributes as follows:
        * source_path (src);
        * destination_path (dst);
        * file_name (fname).

    Parameters
    ----------
    config_file : str
        XML config file path.

    Returns
    -------
    List[Tuple[Path, Path]]
        (src, dst)
    """
    cppaths = []
    root = ET.parse(Path(config_file)).getroot()
    for tag in root.findall('file'):
        fname = tag.get('file_name')
        src = Path(tag.get('source_path')).absolute() / fname
        dst = Path(tag.get('destination_path')).absolute() / fname
        cppaths.append((src, dst))
    return cppaths


# Note.
# It was possible to create SrcDest class with:
#     * dataclass (from dataclasses)
#     * namedtuple (from collections)
# However, the task is simpler, no need to bring complications.

# Concerning copy method, shutil contains copyfile and copy2 as well
# The `copy` function copies not only the content of a file,
# but also its permissions.

# OSErrno 13 is possible if permission denied.

def main():
    """Entry point."""
    cppaths = parse_config_file('./task1.xml')
    for cppath in cppaths:
        src = cppath[0]
        dst = cppath[1]
        print(src)
        print(src.exists())
        if src.exists() and src.is_file():
            if dst.parent.exists():
                copy(src, dst)


if __name__ == '__main__':
    main()
