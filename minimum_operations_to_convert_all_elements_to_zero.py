"""
LeetCode
3542. Minimum Operations to Convert All Elements to Zero
November 2025 Challenge
jramaswami
"""


import dataclasses
from typing import List


@dataclasses.dataclass(frozen=True)
class QItem:
    index: int
    value: int


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.append(0)
        soln = 0
        mtq = [QItem(-1, 0)]
        for i, n in enumerate(nums):

            if mtq[-1].value == n:
                continue

            while mtq[-1].value > n:
                mtq.pop()
                soln += 1
            if mtq[-1].value != n:
                mtq.append(QItem(i, n))

        return soln


def test_3():
    nums = [1,2,1,2,1,2]
    assert Solution().minOperations(nums) == 4