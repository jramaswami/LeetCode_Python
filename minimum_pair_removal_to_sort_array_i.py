"""
LeetCode
3507. Minimum Pair Removal to Sort Array I
January 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(A):
            return all(a <= b for a, b in zip(A[:-1], A[1:]))

        def eliminate(A, j):
            B = []
            for i, n in enumerate(A):
                if i - 1 == j:
                    B[-1] += n
                else:
                    B.append(n)
            return B

        def leftmost_reversal(A):
            curr = None
            for i in range(len(A) - 2, -1, -1):
                if not curr or A[i] + A[i+1] <= curr[0]:
                    curr = (A[i] + A[i+1], i)
            return curr[1]

        A = list(nums)
        soln = 0
        while not is_sorted(A):
            soln += 1
            i = leftmost_reversal(A)
            A = eliminate(A, i)
        return soln