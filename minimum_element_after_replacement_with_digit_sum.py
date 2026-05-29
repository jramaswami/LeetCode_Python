"""
LeetCode
3300. Minimum Element After Replacement With Digit Sum
May 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_digits(n):
            result = 0
            while n:
                n, x = divmod(n, 10)
                result += x
            return result

        return min(sum_digits(n) for n in nums)