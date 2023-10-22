"""
LeetCode
1793. Maqximum Score of a Good Subarray
October 2023 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        soln = nums[k]
        currMin = nums[k]
        currLength = 1
        currLeft = k-1
        currRight = k+1
        while currLength < len(nums):
            leftVal = nums[currLeft] if currLeft >= 0 else -math.inf
            rightVal = nums[currRight] if currRight < len(nums) else -math.inf
            if leftVal >= rightVal:
                currMin = min(currMin, leftVal)
                currLeft -= 1
            else:
                currMin = min(currMin, rightVal)
                currRight += 1
            currLength += 1
            currScore = currLength * currMin
            soln = max(soln, currScore)

        return soln



def test_1():
    nums = [1,4,3,7,4,5]
    k = 3
    expected = 15
    assert Solution().maximumScore(nums, k) == expected


def test_2():
    nums = [5,5,4,5,4,1,1,1]
    k = 0
    expected = 20
    assert Solution().maximumScore(nums, k) == expected