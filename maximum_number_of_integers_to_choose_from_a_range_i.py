"""
LeetCode
2554. Maximum Number of Integers to Choose From a Range I
December 2024 Challenge
jramaswami
"""


class Solution:
    def maxCount(self, banned: List[int], n: int, max_sum: int) -> int:
        banned0 = set(banned)
        curr_sum = 0
        soln = 0
        for x in range(1, n+1):
            if x not in banned0:
                curr_sum += x
                if curr_sum > max_sum:
                    return soln
                soln += 1
        return soln
