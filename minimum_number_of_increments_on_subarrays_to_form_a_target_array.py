"""
LeetCode
1526. Minimum Number of Increments on Subarrays to Form a Target Array
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ns = [0]
        ns.extend(sorted(set(target)))
        soln = 0
        while len(ns) > 1:
            k = ns.pop()
            window = False
            for t in target:
                if t >= k:
                    window = True
                else:
                    if window:
                        soln += (k - ns[-1])
                        window = False
            if window:
                soln += (k - ns[-1])
        return soln