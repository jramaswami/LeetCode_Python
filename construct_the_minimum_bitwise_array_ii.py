"""
LeetCode
3314. Construct the Minimum Bitwise Array II
January 2026 Challenge
jramawami
"""


from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def f(x):
            for n in range(0, x):
                if n | (n+1) == x:
                    return n
            return -1

        return [f(x) for x in nums]


def test_3():
    nums = [884532611,741533369,868936609,816315823,150570781,346594697,334726181,921762641,89355881,403165729,931242733]
    assert Solution().minBitwiseArray(nums) == [0 for _ in nums]