"""
LeetCode
3011. Find if Array Can Be Sorted
November 2024 Challenge
jramaswami
"""


import collections


Item = collections.namedtuple('Item', ['value', 'bits'])


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        A = [Item(x, x.bit_count()) for x in nums]
        swap_made = True
        while swap_made:
            swap_made = False
            for i, x in enumerate(A[:-1]):
                if A[i].value > A[i+1].value and A[i].bits == A[i+1].bits:
                    swap_made = True
                    A[i], A[i+1] = A[i+1], A[i]
        return sorted(A) == A
