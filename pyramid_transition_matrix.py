"""
LeetCode
756. Pyramid Transition Matrix
December 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        patterns = collections.defaultdict(list)
        for p in allowed:
            patterns[p[:-1]].append(p[-1])

        def rec(i, prev_row, curr_row):
            # Base case: done
            if len(curr_row) == 1 and i >= len(curr_row):
                return True
            # Base case: new row
            if i >= len(curr_row):
                next_row = [None for _ in curr_row[:-1]]
                return rec(0, curr_row, next_row)
            # Recursive case
            prefix = prev_row[i] + prev_row[i+1]
            for letter in patterns[prefix]:
                curr_row[i] = letter
                result = rec(i+1, prev_row, curr_row)
                if result:
                    return True
                curr_row[i] = None
            return False

        next_row = [None for _ in bottom[:-1]]
        return rec(0, bottom, next_row)