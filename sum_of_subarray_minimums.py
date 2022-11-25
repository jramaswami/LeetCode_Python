"""
LeetCode :: 907. Sum of Subarray Minimums
November 2022 Challenge
jramaswami

Thank You Larry!
"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = pow(10,9) + 7
        soln = 0
        stack = []
        left = []
        for i, x in enumerate(arr):
            pi = i
            while stack and stack[-1][1] >= x:
                pi, _ = stack.pop()
            left.append(i - pi + 1)
            stack.append((pi, x))

        stack = []
        right = []
        for i, x in enumerate(reversed(arr)):
            pi = i
            while stack and stack[-1][1] > x:
                pi, _ = stack.pop()
            right.append(i - pi + 1)
            stack.append((pi, x))

        right.reverse()
        for x, L, R in zip(arr, left, right):
            soln += L * R * x
            soln %= MOD

        return soln % MOD