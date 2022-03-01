"""
LeetCode :: March 2022 Challenge :: Counting Bits
jramaswami
"""


class Solution:

    def countBits(self, n):
        bits = [-1 for _ in range(n+1)]
        bits[0] = 0
        for i in range(n+1):
            if bits[i] == -1:
                raise Exception(f"{i} has not been set yet!")
            j = (i << 1)
            k = j | 1
            if j < len(bits):
                bits[j] = bits[i]
            if k < len(bits):
                bits[k] = bits[i] + 1
        return bits


def test_1():
    n = 2
    expected = [0,1,1]
    assert Solution().countBits(n) == expected


def test_2():
    n = 5
    expected = [0,1,1,2,1,2]
    assert Solution().countBits(n) == expected
