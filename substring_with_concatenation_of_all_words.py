"""
LeetCode :: August 2022 Chalenge :: 30. Substring with Concatenation of All Words
jramaswami
"""


from typing import *
import collections


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        words0 = collections.Counter(words)
        intervals = []
        for i, _ in enumerate(s):
            if i + k > len(s):
                break
            if s[i:i+k] in words0:
                intervals.append((i, i+k))

        print(intervals)
        soln = []
        for i, (a, b) in enumerate(intervals):
            print(f"{a=} {b=} {s[a:b]=}")
            curr = collections.defaultdict(int)
            prev_stop = a
            words_found = 0
            for j, (x, y) in enumerate(intervals[i:]):
                print(f"{x=} {y=} {s[x:y]=} {curr=}")
                if prev_stop != x:
                    print('gap')
                    break
                t = s[x:y]
                if curr[t] == words0[t]:
                    print(f"too many {t}")
                    break
                curr[t] +=1
                words_found += 1
                print(f"{words_found=} {len(words)=}")
                if words_found == len(words):
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