"""
LeetCode
3304. Find the K-th Character in String Game I
July 2025 Challenge
jramaswami
"""


class Solution:
    def kthCharacter(self, k: int) -> str:
        # string increases by powers of 2
        # 1 <= k <= 500
        # max operation is 9 because 2^9 = 512
        # brute force
        def shift(c):
            x = ord(c) - ord('a')
            x = (x + 1) % 26
            return chr(x + ord('a'))

        def f(s):
            t = [shift(c) for c in s]
            return f'{s}{"".join(t)}'

        s = "a"
        while len(s) < k:
            s = f(s)
        return s[k-1]


def test_1():
    k = 5
    expected = "b"
    assert Solution().kthCharacter(k) == expected