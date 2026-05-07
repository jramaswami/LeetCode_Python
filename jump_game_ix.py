"""
LeetCode
3660. Jump Game IX
May 2026 Challenge
jramaswami

REF: https://algo.monster/liteproblems/3660
"""


from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        INF = pow(10, 10)
        soln = [0 for _ in nums]
        pre_max =[nums[0] for _ in nums]
        for i, n in enumerate(nums[1:], start=1):
            pre_max[i] = max(pre_max[i-1], n)
        suf_min = INF
        for i in range(len(nums)-1, -1, -1):
            if i+1 < len(nums):
                soln[i] = soln[i+1] if pre_max[i] > suf_min else pre_max[i]
            else:
                soln[i] = pre_max[i] if pre_max[i] <= suf_min else 0
            suf_min = min(suf_min, nums[i])
        return soln


def test_1():
    nums = [2,3,1]
    expected = [3,3,3]
    assert Solution().maxValue(nums) == expected