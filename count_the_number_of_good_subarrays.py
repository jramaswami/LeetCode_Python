"""
LeetCode
2537. Count the Number of Good Subarrays
April 2025 Challenge
jramaswami
"""


from typing import List
import collections


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        soln = 0
        window = collections.deque()
        freqs = collections.Counter()
        curr_pairs = 0
        for right, x in enumerate(nums):
            # Add to window
            curr_pairs += freqs[x]
            freqs[x] += 1
            window.append(x)
            while curr_pairs >= k:
                print(window, freqs, right)
                # From right to the end there are enough
                soln += (len(nums) - right)
                # Remove leftmost from window
                y = window.popleft()
                freqs[y] -= 1
                curr_pairs -= freqs[y]
        return soln


def test_1():
    nums = [1,1,1,1,1]
    k = 10
    expected = 1
    assert Solution().countGood(nums, k) == expected


def test_2():
    nums = [3,1,4,3,2,2,4]
    k = 2
    expected = 4
    assert Solution().countGood(nums, k) == expected


def test_3():
    nums = [2,3,3,3,3,1,3,1,3,2]
    k = 19
    expected = 0
    assert Solution().countGood(nums, k) == expected