"""
LeetCode :: August 2022 Chalenge :: 30. Substring with Concatenation of All Words
jramaswami
"""


from typing import *
import collections


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        m = len(words) * k
        words0 = collections.Counter(words)
        intervals = set()
        for i, _ in enumerate(s):
            if i + k > len(s):
                break
            if s[i:i+k] in words0:
                intervals.add((i, i+k))

        def check(start_at):
            curr = collections.defaultdict(int)
            a = start_at
            for _ in range(len(words)):
                if a+k > len(s):
                    return False
                if (a, a+k) in intervals:
                    t = s[a:a+k]
                    curr[t] += 1
                    if curr[t] > words0[t]:
                        return False
                else:
                    return False
                a += k
            return True

        return [i for i, _ in enumerate(s) if check(i)]


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

def test_5():
    "WA"
    s = "a"
    words = ["a"]
    expected = [0]
    assert Solution().findSubstring(s, words) == expected


def test_6():
    "WA"
    s = "ababababab"
    words = ["ababa","babab"]
    expected = [0]
    assert Solution().findSubstring(s, words) == expected