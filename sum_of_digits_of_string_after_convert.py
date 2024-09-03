"""
LeetCode
1945. Sum of Digits of String After Convert
September 2024 Challenge
jramaswami
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(x):
            return str(sum(int(c) for c in x))

        result = "".join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            result = transform(result)
        return int(result)
