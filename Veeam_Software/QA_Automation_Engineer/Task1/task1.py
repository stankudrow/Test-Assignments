#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Veeam Software Test Assignment 1."""


import xml.etree.ElementTree as ET

from dataclasses import dataclass
from pathlib import Path
from shutil import copy
from typing import List


@dataclass
class SDF:
    """Source Destination Filename dataclass."""

    src: Path
    dst: Path


def parse_config_file(config_file: str) -> List[SDF]:
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
    List[SDF]

    """
    cppaths = []
    root = ET.parse(Path(config_file)).getroot()
    for tag in root.findall("file"):
        fname = tag.get("file_name")
        src = Path(tag.get("source_path")).resolve() / fname
        dst = Path(tag.get("destination_path")).resolve() / fname
        cppaths.append(SDF(src, dst))
    return cppaths


# Concerning copy method, shutil contains copyfile and copy2 as well
# The `copy` function copies not only the content of a file,
# but also its permissions.

# OSErrno 13 is possible if permission denied.


def main():
    """Entry point."""
    cppaths = parse_config_file("./task1.xml")
    for cppath in cppaths:
        src = cppath.src
        dst = cppath.dst
        if src.exists() and src.is_file():
            if dst.parent.exists():
                copy(src, dst)


if __name__ == "__main__":
    main()
