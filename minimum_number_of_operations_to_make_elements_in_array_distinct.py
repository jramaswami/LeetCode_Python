"""
LeetCode
3396. Minimum Number of Operations to Make Elements in Array Distinct
April 2025 Challenge
jramaswami
"""


from typing import List
import collections
import itertools


def batched_generator(iterable, n):
    iterator = iter(iterable)
    while batch := tuple(itertools.islice(iterator, n)):
        yield batch


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freqs = collections.Counter(nums)
        multis = sum(1 if f > 1 else 0 for f in freqs.values())
        soln = 0
        for batch in batched_generator(nums, 3):
            if multis == 0:
                break
            soln += 1
            for x in batch:
                freqs[x] -= 1
                if freqs[x] == 1:
                    multis -= 1
        return soln