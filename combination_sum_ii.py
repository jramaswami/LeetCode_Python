"""
LeetCode
40. Combination Sum II
jramaswami
"""


import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        soln = set()
        candidates.sort()
        freqs = tuple((val, freq) for val, freq in collections.Counter(candidates).items())

        def rec(i, acc, curr_sum):
            if curr_sum == target:
                soln.add(acc)
                return

            if i >= len(freqs):
                return

            if curr_sum > target:
                return

            rec(i+1, acc, curr_sum)
            val, freq = freqs[i]

            t = list(acc)
            for k in range(1, freq+1):
                curr_sum += val
                t.append(val)
                rec(i+1, tuple(t), curr_sum)

        rec(0, [], 0)
        return [list(t) for t in soln]