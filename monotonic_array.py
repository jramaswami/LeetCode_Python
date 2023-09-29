"""
LeetCode
896. Monotonic Array
September 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        def isMonotonicIncreasing(arr):
            for a, b in zip(arr[:-1], arr[1:]):
                if a > b:
                    return False
            return True

        def isMonotonicDecreasing(arr):
            for a, b in zip(arr[:-1], arr[1:]):
                if a < b:
                    return False
            return True

        return isMonotonicIncreasing(nums) or isMonotonicDecreasing(nums)


def test_1():
    nums = [1,2,2,3]
    assert Solution().isMonotonic(nums) == True


def test_2():
    nums = [6,5,4,4]
    assert Solution().isMonotonic(nums) == True


def test_3():
    nums = [1,3,2]
    assert Solution().isMonotonic(nums) == False