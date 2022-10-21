"""
LeetCode :: October 2022 Challenge :: 219. Contains Duplicate II
jramaswami
"""


import collections
import math
from typing import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_occurrence = collections.defaultdict(lambda: -math.inf)
        for i, n in enumerate(nums):
            if i - last_occurrence[n] <= k:
                return True
            last_occurrence[n] = i
        return False


def test_1():
    nums = [1,2,3,1]
    k = 3
    expected = True
    assert Solution().containsNearbyDuplicate(nums, k) == expected


def test_2():
    nums = [1,0,1,1]
    k = 1
    expected = True
    assert Solution().containsNearbyDuplicate(nums, k) == expected


def test_3():
    nums = [1,2,3,1,2,3]
    k = 2
    expected = False
    assert Solution().containsNearbyDuplicate(nums, k) == expected