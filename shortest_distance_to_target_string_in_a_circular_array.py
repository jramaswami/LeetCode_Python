"""
LeetCode
2515. Shortest Distance to Target String in a Circular Array
April 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        INF = pow(10, 10)
        soln = INF
        N = len(words)
        for i, word in enumerate(words):
            if word == target:
                soln = min(soln, (N + i - startIndex) % N)
                soln = min(soln, (N + startIndex - i) % N)
        return soln if soln < INF else -1