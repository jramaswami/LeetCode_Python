"""
LeetCode
2418. Sort the People
July 2024 Challenge
jramaswami
"""


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [t[1] for t in sorted((-h, n) for n, h in zip(names, heights))]