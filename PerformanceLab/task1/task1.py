from collections import deque
from sys import argv
from typing import List


def generate_sequence(num: int) -> List[int]:
	return list(range(1, num + 1))

def sanitise_input(nums: List[int], nval: int) -> None:
	if not nums:
		raise ValueError(f"{nums} is invalid")
	if interval < 1:
		raise ValueError(f"{nval} is invalid")
	numset = set(nums)
	if len(numset) != len(nums):
		raise ValueError("duplicate numbers")
	for num in numset:
		if not (0 < num < 10):
			raise ValueError(f"not 1 <= {num} <= 9")

def get_paths(nums: List[int], nval: int) -> List[str]:
	if len(nums) == 1:
		return nums
	seq = []
	dnums = deque(nums)
	rot = -(nval - 1)
	while True:
		seq.append(dnums[0])
		dnums.rotate(rot)
		if seq[0] == dnums[0]:
			break
	return seq


if __name__ == '__main__':
	if len(argv[1:3]) == 2:
		nums = generate_sequence(int(argv[1]))
		interval = int(argv[2])
		sanitise_input(nums, interval)
		paths = get_paths(nums, interval)
		print(''.join(str(path) for path in paths))