"""
LeetCode :: August 2022 Chalenge :: 30. Substring with Concatenation of All Words
jramaswami
"""


from typing import *


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        words0 = set(words)
        intervals = []
        for i, _ in enumerate(s):
            if i + k >= len(s):
                break
            if s[i:i+k] in words0:
                intervals.append((i, i+k))

        soln = []
        for i, (a, b) in enumerate(intervals):
            curr = set([s[a:b]])
            prev_stop = b
            for j, (x, y) in enumerate(intervals[i+1:]):
                if prev_stop != x:
                    break
                t = s[x:y]
                if t in curr:
                    break
                curr.add(t)
                if len(curr) == len(words):
                    soln.append(a)
                    break
                prev_stop = y

        return soln


def test_1():
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    expected = [0,9]
    assert Solution().findSubstring(s, words) == expected


def test_2():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    expected = []
    assert Solution().findSubstring(s, words) == expected


def test_3():
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    expected = [6,9,12]
    assert Solution().findSubstring(s, words) == expected


def test_4():
    "WA"
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    expected = [8]
    assert Solution().findSubstring(s, words) == expected