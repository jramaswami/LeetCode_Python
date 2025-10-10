"""
LeetCode
3147. Taking Maximum Energy From the Mystic Dungeon
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        energy0 = energy[::-1]
        dp = [0 for _ in energy]
        dp[:k] = list(energy0[:k])
        for i, m in enumerate(energy0[k:], start=k):
            dp[i] = m + dp[i-k]
        return max(dp)