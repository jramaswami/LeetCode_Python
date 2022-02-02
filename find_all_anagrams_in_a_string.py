"""
LeetCode :: February 2022 Challenge :: 438. Find All Anagrams in a String
jramaswami
"""


class Solution:

    def findAnagrams(self, s, p):

        prefix = [[] for _ in s]
        EMPTY = [0 for _ in range(26)]

        def check(left, right, target):
            for a, b, t in zip(left, right, target):
                if b - a != t:
                    return False
            return True

        def get_prefix(i):
            if i < 0:
                return EMPTY
            return prefix[i]

        ord_a = ord('a')
        target = list(EMPTY)
        for c in p:
            target[ord(c) - ord_a] += 1

        soln = []
        prefix[0] = list(EMPTY)
        prefix[0][ord(s[0]) - ord_a] += 1
        for i, c in enumerate(s[1:], start=1):
            prefix[i] = list(prefix[i-1])
            prefix[i][ord(c) - ord_a] += 1

            if check(get_prefix(i-len(p)), prefix[i], target):
                soln.append(i - len(p) + 1)

        return soln


def test_1():
    s = "cbaebabacd"
    p = "abc"
    expected = [0,6]
    assert Solution().findAnagrams(s, p) == expected


def test_2():
    s = "abab"
    p = "ab"
    expected = [0,1,2]
    assert Solution().findAnagrams(s, p) == expected


def test_3():
    "WA"
    s = "aecbabedce"
    p = "a"
    expected = [0, 4]
    assert Solution().findAnagrams(s, p) == expected

