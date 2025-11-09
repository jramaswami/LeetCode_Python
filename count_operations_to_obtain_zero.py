"""
LeetCode
2169. Count Operations to Obtain Zero
November 2025 Challenge
jramaswami
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        soln = 0
        while num1 and num2:
            soln += 1
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
        return soln