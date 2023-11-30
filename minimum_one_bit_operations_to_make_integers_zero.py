"""
LeetCode
1611. Minimum One Bit Operations to Make Integers Zero
November 2023 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=yRI18_MaG7k
"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Base case
        if n == 0:
            return 0

        # Find the most significant bit.
        k = 0
        while pow(2, k) <= n:
            k += 1
        k -= 1

        n0 = pow(2, k) ^ n
        return pow(2, k+1) - 1 - self.minimumOneBitOperations(n0)