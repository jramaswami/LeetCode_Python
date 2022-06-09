"""
LeetCode :: June 2022 Challenge :: 167. Two Sum II - Input Array Is Sorted
jramaswami
"""


import bisect


class Solution:
    def twoSum(self, numbers, target):
        for i, n in enumerate(numbers):
            j = bisect.bisect_left(numbers, target-n, lo=i+1)
            if j < len(numbers) and numbers[j] == target-n:
                return [i+1, j+1]


def test_1():
    numbers = [2,7,11,15]
    target = 9
    expected = [1,2]
    assert Solution().twoSum(numbers, target) == expected


def test_2():
    numbers = [2,3,4]
    target = 6
    expected = [1,3]
    assert Solution().twoSum(numbers, target) == expected


def test_3():
    numbers = [-1,0]
    target = -1
    expected = [1,2]
    assert Solution().twoSum(numbers, target) == expected
