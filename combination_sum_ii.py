"""
LeetCode
40. Combination Sum II
jramaswami
"""


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        soln = set()
        candidates.sort()

        def rec(i, acc, curr_sum):
            if curr_sum == target:
                soln.add(tuple(acc))
                return

            if i >= len(candidates):
                return

            if curr_sum > target:
                return

            # Without candidates[i]
            rec(i+1, acc, curr_sum)

            # With candidates[i]
            acc.append(candidates[i])
            rec(i+1, acc, curr_sum + candidates[i])
            acc.pop()

        rec(0, [], 0)
        return [list(t) for t in soln]