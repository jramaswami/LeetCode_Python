"""
LeetCode
1550. Three Consecutive Odds
July 2024 Challenge
jramaswami
"""


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0
        for n in arr:
            if n % 2:
                consecutive_odds += 1
            else:
                consecutive_odds = 0
            if consecutive_odds >= 3:
                return True
        return False
