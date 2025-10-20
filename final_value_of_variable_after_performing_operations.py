"""
LeetCode
2011. Final Value of Variable After Performing Operations
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        soln = 0
        for op in operations:
            if op in ('++X', 'X++'):
                soln += 1
            elif op in ('--X', 'X--'):
                soln -= 1
        return soln