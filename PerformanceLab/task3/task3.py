from collections import ChainMap
import json
from os import PathLike
from sys import argv
from typing import Dict


def form_report(tests: Dict, values: Dict) -> Dict:
    def map_data(tdata: Dict, vdata: Dict) -> None:
        for tdatum in tdata:
            testid = tdatum["id"]
            for testval in vdata:
                if testval["id"] == testid:
                    tdatum["value"] = testval["value"]
                    break
            if "values" in tdatum:
                map_data(tdatum["values"], vdata)

    tests_data = tests["tests"]
    values_data = values["values"]
    map_data(tests_data, values_data)
    return {"report": tests_data}


def main(tests: str, values: str, report: str) -> None:
    with open(tests) as tfl, open(values) as vfl:
        dtests: Dict = json.load(tfl)
        dvalues: Dict = json.load(vfl)
        with open(report, "w") as rfl:
            dreport = form_report(dtests, dvalues)
            json.dump(dreport, rfl, indent=4)


if __name__ == "__main__":
    argc = len(argv[1:])
    if argc in (2, 3):
        out = argv[3] if argc == 3 else "report.json"
        main(argv[1], argv[2], out)
