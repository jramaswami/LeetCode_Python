"""
LeetCode :: December 2021 Challenge :: 231. Power of Two
jramaswami
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powers = [pow(2, i) for i in range(33)]
        try:
            i = powers.index(n)
            return True
        except:
            return False
