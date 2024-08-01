"""
LeetCode
2678. Number of Senior Citizens
August 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 if int(t[11:13]) > 60 else 0 for t in details)