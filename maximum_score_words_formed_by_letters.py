"""
LeetCode
1255. Maximum Score Words Formed by Letters
May 2024 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        words0 = [collections.Counter(w) for w in words]
        letters0 = collections.Counter(letters)

        def get_score(word):
            return sum(score[ord(c) - ord('a')] * f for c, f in word.items())

        def can_choose(word):
            return all(letters0[c] >= f for c, f in word.items())

        def remove_word(word):
            for c, f in word.items():
                letters0[c] -= f

        def add_word(word):
            for c, f in word.items():
                letters0[c] += f

        def rec(i):
            if i >= len(words0):
                return 0

            word = words0[i]
            result = rec(i+1)
            if can_choose(word):
                remove_word(word)
                word_score = get_score(word)
                result = max(result, word_score + rec(i+1))
                add_word(word)
            return result

        return rec(0)


def test_1():
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    expected = 23
    result = Solution().maxScoreWords(words, letters, score)
    assert result == expected


def test_2():
    words = ["xxxz","ax","bx","cx"]
    letters = ["z","a","b","c","x","x","x"]
    score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    expected = 27
    result = Solution().maxScoreWords(words, letters, score)
    assert result == expected


def test_3():
    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    expected = 0
    result = Solution().maxScoreWords(words, letters, score)
    assert result == expected