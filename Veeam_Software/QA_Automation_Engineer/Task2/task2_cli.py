#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Veeam Software Test Assignment 2: CLI."""


from typing import Dict

import click

import task2


@click.command()
@click.option("-f", "--file", nargs=1, type=str, default=None, show_default=True)
@click.argument("infile", nargs=1)
@click.argument("dirpath", nargs=1)
def cli(infile, dirpath, file):
    """
    Check files integrity at dirpath comparing with data from infile.

    Print statistics either in stdout or in a file.

    Parameters
    ----------
    infile : str
        `filename-hash_algorithm-hash_sum` data.
    dirpath : str
        search for files to check.
    file : str, optional
        file to write results to.

    Returns
    -------
    str
        files-statuses.

    """
    data = task2.parse_infile(infile)
    stats = task2.check_files(data, dirpath)
    resstr = get_files_stats(stats)
    if file is not None:
        with open(file, "w") as inf:
            click.echo(message=resstr, file=inf)
    else:
        click.echo(message=resstr)


def get_files_stats(fstats: Dict[str, str]) -> str:
    """
    Return string with `filename status` lines.

    Parameters
    ----------
    fstats : Dict[str, str]
        {filename: status}

    Returns
    -------
    str

    """
    res = ""
    for fname in sorted(fstats):
        res += f"{fname} {fstats[fname]}\n"
    return res


# pylint: disable=no-value-for-parameter


if __name__ == "__main__":
    cli()
