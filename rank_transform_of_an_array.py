"""
LeetCode
1331. Rank Transform of an Array
October 2024 Challenge
jramaswami
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # O(n log n)
        order = sorted((x, i) for i, x in enumerate(arr))
        # O(n)
        rank = [0 for _ in arr]
        curr_rank = 0
        prev_value = None
        # O(n)
        for x, i in order:
            if x != prev_value:
                curr_rank += 1
            rank[i] = curr_rank
            prev_value = x
        return rank
