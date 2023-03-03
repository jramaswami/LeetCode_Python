"""
LeetCode
28. Find the Index of the First Occurrence in a String
March 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Rabin-Karp
        base = 27
        big_prime = 10089886811898868001
        needle_hash = 0
        ord_a = ord('a')
        for t in needle:
            x = ord(t) - ord_a + 1
            needle_hash = (needle_hash * base) % big_prime
            needle_hash = (needle_hash + x) % big_prime
        exp = len(needle) - 1
        hi_pow = pow(base, exp, big_prime)
        window = collections.deque()
        curr_hash = 0
        for i, t in enumerate(haystack):
            if len(window) == len(needle):
                x = ord(window[0]) - ord_a + 1
                x = (x * hi_pow) % big_prime
                curr_hash -= x
                window.popleft()
            window.append(t)
            x = ord(t) - ord_a + 1
            curr_hash = (curr_hash * base) % big_prime
            curr_hash = (curr_hash + x) % big_prime
            if curr_hash == needle_hash:
                if "".join(window) == needle:
                    return i - len(needle) + 1
        return -1


def test_1():
    haystack = "sadbutsad"
    needle = "sad"
    expected = 0
    assert Solution().strStr(haystack, needle) == expected


def test_2():
    haystack = "leetcode"
    needle = "leeto"
    expected = -1
    assert Solution().strStr(haystack, needle) == expected