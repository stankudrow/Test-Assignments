#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Veeam Software Test Assignment 2."""


from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Union

from task2_core import hash_file


PathType = Union[str, Path]


@dataclass
class FAS:
    """FileName HashAlgorithm HashSum dataclass."""

    filename: str
    hashalgo: str
    hashsum: str


def parse_infile(filepath: PathType) -> List[FAS]:
    """
    Parse input file with `filename hash_algorithm hash_sum` lines.

    Parameters
    ----------
    filepath : PathType

    Returns
    -------
    List[FAS]

    """
    records = {}
    with open(filepath) as infile:
        for line in infile:
            line_spl = line.split()
            if len(line_spl) == 3:
                records[line_spl[0]] = FAS(*line_spl)
    return list(records.values())


def check_files(records: Iterable[FAS], dirpath: PathType) -> Dict[str, str]:
    """
    Check files integrity at dirpath comparing with data from records.

    Parameters
    ----------
    records : Iterable[FAS]
        (filename, hash_algo, hash_sum).
    dirpath : PathType
        the directory with files to check.

    Returns
    -------
    Dict[str, str]
        {filename: status}.

    """
    dpath = Path(dirpath)
    stats = {entry.name: "" for entry in dpath.iterdir() if entry.is_file()}
    for record in records:
        rec_fname = record.filename
        sts_fname = stats.get(rec_fname)
        if sts_fname is None:
            stats[rec_fname] = "NOT FOUND"
        else:
            sts_fhash = hash_file(dpath / rec_fname, record.hashalgo)
            if sts_fhash == record.hashsum:
                stats[rec_fname] = "OK"
            else:
                stats[rec_fname] = "FAIL"
    return stats


# unnecessary
if __name__ == "__main__":
    fas_records = parse_infile("task2_input.txt")
    print(check_files(fas_records, "outfiles"))
