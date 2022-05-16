from pytest import mark

from task4 import get_shortest_reduce


@mark.parametrize(
    "nums, res",
    [
        ([], 0),
        ([1], 0),
        ([1, 1], 0),
        ([1, 2], 1),
        ([3, 2, 1], 2),
        ([2, 1, 1, 2], 2),
        ([1, 10, 2, 9], 16),
    ],
)
def test_task4(nums, res):
    assert get_shortest_reduce(nums) == res
