#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Veeam Software Test Assignment 2.

Module containing program main logic.
"""


from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Union

from task2_core import hash_file


PathType = Union[str, Path]


@dataclass
class HashRecord:
    """Filename Hash_algorithm Hash_sum record."""

    filename: str
    algo: str
    hash: str


def parse_infile(filepath: PathType) -> List[HashRecord]:
    """
    Parse input file with files to check.

    Each significant line contains `filename hash_algorithm hash_sum`.

    Parameters
    ----------
    filepath : PathType

    Returns
    -------
    Dict[str, HashRecord]

    """
    records = {}
    with open(filepath) as infile:
        for line in infile:
            line = line.split()
            if len(line) == 3:
                records[line[0]] = HashRecord(*line)  # test it!!!
    return list(records.values())


def check_files(records: Iterable[HashRecord], dirpath: PathType) -> Dict[str, str]:
    """
    Check files integrity at dirpath comparing with data from records.

    Parameters
    ----------
    records : Iterable[HashRecord]
        DESCRIPTION.
    dirpath : PathType
        DESCRIPTION.

    Returns
    -------
    Dict[str, str]
        DESCRIPTION.

    """
    dpath = Path(dirpath)
    stats = {entry.name: object for entry in dpath.iterdir() if entry.is_file()}
    for record in records:
        rec_fname = record.filename
        sts_fname = stats.get(rec_fname)
        if sts_fname is None:
            stats[rec_fname] = "NOT FOUND"
        else:
            sts_fhash = hash_file(dpath / rec_fname, record.algo)
            if sts_fhash == record.hash:
                stats[rec_fname] = "OK"
            else:
                stats[rec_fname] = "FAIL"
    return stats


# unnecessary
if __name__ == "__main__":
    records = parse_infile("task2_input.txt")
    print(check_files(records, "outfiles"))
