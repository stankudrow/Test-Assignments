#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 - data parsing."""


__author__ = "Stanislav D. Kudriavtsev"


import json

from pathlib import Path
from sys import exit


# Attention.
# the original files were with mistakes
# so they all were passed through JSON
# online validator and beautifier, see
# README in files/cleaned directory
def get_task_data():
    """Return the test files parsed.

    Returns
    -------
    data : dict
      test files for task1
    """
    keyfiles = ["error", "struct", "testcase", "values"]
    data = {}
    for keyfile in keyfiles:
        fpath = Path() / "files" / "cleaned" / f"{keyfile}.json"
        try:
            with open(fpath) as jf:
                data[keyfile] = json.load(jf)
        except Exception as exc:
            print(f"The file {fpath} failed")
            print(f"the exception caught -> {exc}")
            print("./error.json file has been formed")
            with open("error.json", "w", encoding="utf-8") as erf:
                erc = {"error": {"message": "Входные файлы некорректны"}}
                json.dump(erc, erf, ensure_ascii=False)
            exit(1)
    return data


def process_task(testcase: dict, values: dict):
    """Process testcase with values."""
    for tcparam in testcase["params"]:
        if not tcparam.get("values"):
            for vvalue in values["values"]:
                if tcparam["id"] == vvalue["id"]:
                    tcparam["value"] = vvalue["value"]
                # else no change is required
        else:
            for pvalue in tcparam["values"]:
                if pvalue.get("params"):
                    newpars = {"params": pvalue["params"]}
                    pvalue["params"] = process_task(newpars, values)["params"]
                for vvalue in values["values"]:
                    if pvalue["id"] == vvalue["value"]:
                        tcparam["value"] = pvalue["title"]
    return testcase


def main():
    """Entry point."""
    data = get_task_data()
    testcase, values = data["testcase"], data["values"]
    return process_task(testcase, values)


if __name__ == "__main__":
    print(main())
