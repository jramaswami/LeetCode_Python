"""
LeetCode
2311. Longest Binary Subsequence Less Than or Equal to K
June 2025 Challenge
jramaswami
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        bit_value = pow(2, len(s)-1)
        total_value = int(s, 2)
        bits_removed = 0
        for bit in s:
            if bit == '1' and total_value > k:
                bits_removed += 1
                total_value -= bit_value
            bit_value //= 2
        return len(s) - bits_removed