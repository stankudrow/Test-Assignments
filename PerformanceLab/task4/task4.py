from collections import Counter
from functools import reduce
from sys import argv
from typing import Iterable


def get_shortest_reduce(nums: Iterable[int]) -> int:
    if not nums:
        return 0
    cnt = Counter(nums)
    diffs = []
    for ck, cv in cnt.items():
        sum_ = sum(abs(ck - k) * cv for k in cnt.keys())
        diffs.append(sum_)
    return min(diffs)


if __name__ == "__main__":
    if len(argv[1:]) == 1:
        with open(argv[1]) as fl:
            numbers = (int(line) for line in fl.readlines())
            print(get_shortest_reduce(numbers))
