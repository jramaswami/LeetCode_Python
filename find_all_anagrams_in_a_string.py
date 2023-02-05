"""
LeetCode
438. Find All Anagrams in a String
February 2023 Challenge
jramaswami
"""

import string
import collections


class Solution:

    def findAnagrams(self, s, p):

        def eq(a, b):
            for c in string.ascii_lowercase:
                if a.get(c, 0) != b.get(c, 0):
                    return False
            return True


        pfreqs = collections.Counter(p)
        wfreqs = collections.Counter()

        window = collections.deque()
        soln = []
        for i, c in enumerate(s):
            # Add letter to window.
            wfreqs[c] += 1
            window.append(c)
            # Size window.
            if len(window) > len(p):
                wfreqs[window[0]] -= 1
                window.popleft()
            if eq(pfreqs, wfreqs):
                soln.append(i-len(p)+1)
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
