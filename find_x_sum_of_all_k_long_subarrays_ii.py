"""
LeetCode
3318. Find X-Sum of All K-Long Subarrays II
November 2025 Challenge
jramaswami
"""


import collections
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        soln = []
        freqs = collections.Counter()
        window = collections.deque()
        top = SortedSet()
        bottom = SortedSet()
        curr = 0
        for n in nums:
            # Remove old key from appropriate set
            if freqs[n] > 0:
                old_key = (freqs[n], n)
                if old_key in top:
                    top.remove(old_key)
                    curr -= (old_key[0] * old_key[1])
                else:
                    bottom.remove(old_key)
            # Add n to window and new key to bottom set
            freqs[n] += 1
            window.append(n)
            new_key = (freqs[n], n)
            bottom.add(new_key)

            # Invariant : len(window) <= k
            while len(window) > k:
                m = window.popleft()
                # Remove old key from appropriate set
                old_key = (freqs[m], m)
                if old_key in top:
                    top.remove(old_key)
                    curr -= (old_key[0] * old_key[1])
                else:
                    bottom.remove(old_key)
                freqs[m] -= 1

                # Add new key to bottom
                if freqs[m] > 0:
                    new_key = (freqs[m], m)
                    bottom.add(new_key)

            # Invariant: put up to x values in top and the
            # remainder in bottom
            while bottom and len(top) < x:
                # Remove largest key from bottom
                new_key = bottom[-1]
                bottom.remove(new_key)
                # Put it in the top
                top.add(new_key)
                # Adjust running total
                curr += (new_key[0] * new_key[1])

            # Invariant: largest bottom is smaller than smallest top
            while bottom and bottom[-1] > top[0]:
                old_key = top[0]
                curr -= (old_key[0] * old_key[1])
                top.remove(old_key)
                bottom.add(old_key)
                new_key = bottom[-1]
                curr += (new_key[0] * new_key[1])
                bottom.remove(new_key)
                top.add(new_key)

            if len(window) == k:
                soln.append(curr)

        return soln