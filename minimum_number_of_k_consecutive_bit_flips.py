"""
LeetCode :: 995. Minimum Number of K Consecutive Bit Flips
jramaswami
"""


import collections


class Solution:

    def minKBitFlips(self, bits, k):
        soln = 0
        flips = collections.deque()
        for i, _ in enumerate(bits):
            if flips and flips[0] <= i:
                flips.popleft()
            b = (bits[i] + len(flips)) % 2
            if b == 0:
                if i + k <= len(bits):
                    flips.append(i+k)
                    soln += 1
                else:
                    return -1
        return soln


def test_1():
    nums = [0,1,0]
    k = 1
    expected = 2
    assert Solution().minKBitFlips(nums, k) == expected


def test_2():
    nums = [1,1,0]
    k = 2
    expected = -1
    assert Solution().minKBitFlips(nums, k) == expected


def test_3():
    nums = [0,0,0,1,0,1,1,0]
    k = 3
    expected = 3
    assert Solution().minKBitFlips(nums, k) == expected
