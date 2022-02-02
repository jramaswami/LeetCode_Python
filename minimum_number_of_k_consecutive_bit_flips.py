"""
LeetCode :: 995. Minimum Number of K Consecutive Bit Flips
jramaswami
"""


class Solution:

    def minKBitFlips(self, bits, k):

        def flip(i):
            bits[i:i+k] = [not b for b in bits[i:i+k]]

        soln = 0
        for i, _ in enumerate(bits):
            if bits[i] == 0:
                if i + k <= len(bits):
                    flip(i)
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
