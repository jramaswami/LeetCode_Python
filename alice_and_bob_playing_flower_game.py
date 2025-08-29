"""
LeetCode
3021. Alice and Bob Playing Flower Game
August 2025 Challenge
jramaswami
"""


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_n = n // 2
        odd_n = even_n + (n % 2)
        even_m = m // 2
        odd_m = even_m + (m % 2)
        return (even_n * odd_m) + (odd_n * even_m)
