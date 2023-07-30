"""
LeetCode
664. Strange Printer
July 2023 Challenge
jramaswami
REF: https://algo.monster/liteproblems/664
"""


import functools


class Solution:
    def strangePrinter(self, s: str) -> int:
        @functools.cache
        def rec(left, right):
            if left > right:
                return 0
            result = rec(left+1, right) + 1
            for mid in range(left+1, right+1):
                if s[mid] == s[left]:
                    result = min(result, rec(left, mid-1) + rec(mid+1, right))
            return result

        return rec(0, len(s)-1)



def test_1():
    s = "aaabbb"
    expected = 2
    assert Solution().strangePrinter(s) == expected


def test_2():
    s = "aba"
    expected = 2
    assert Solution().strangePrinter(s) == expected