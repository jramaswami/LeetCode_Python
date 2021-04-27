"""
Leet Code :: April 2021 Challenge :: Power of Three
jramaswami
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return 1162261467 % n == 0 if n > 0 else False