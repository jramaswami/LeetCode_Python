"""
LeetCode
3719. Longest Balanced Subarray I
February 2026 Challenge
jramaswami
"""


import collections


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        def check(k):
            if k == 0:
                return True
            freqs = collections.Counter()
            parity = [0, 0]
            window = collections.deque()
            for n in nums:
                window.append(n)
                if freqs[n]:
                    freqs[n] += 1
                else:
                    freqs[n] = 1
                    parity[n % 2] += 1
                while len(window) > k:
                    x = window.popleft()
                    freqs[x] -= 1
                    if freqs[x] == 0:
                        parity[x % 2] -= 1
                if len(window) == k and parity[0] == parity[1]:
                    return True
            return False

        for length in range(len(nums), -1, -1):
            if check(length):
                return length
        return 0
