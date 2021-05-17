"""
LeetCode :: May 2021 Challenge :: Longest String Chain
jramaswami
"""
from typing import *
from collections import namedtuple, defaultdict


WordData = namedtuple('WordData', ['word', 'index'])


def can_chain(word_left, word_right):
    """
    Return True if word_left can become word_right with the addition of one
    letter.  
    """
    delta = 0
    left_index = 0
    right_index = 0
    while left_index < len(word_left.word):
        if word_left.word[left_index] != word_right.word[right_index]:
            if delta:
                return False
            right_index += 1
            delta = 1
        else:
            left_index += 1
            right_index += 1

    return True


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words0 = defaultdict(list)
        dp = [1 for _ in words]
        word_lengths = set()
        for w in (WordData(w, i) for i, w in enumerate(words)):
            word_lengths.add(len(w.word))
            words0[len(w.word)].append(w)

        for length in sorted(word_lengths):
            if length + 1 in word_lengths:
                for word_left in words0[length]:
                    for word_right in words0[length + 1]:
                        if can_chain(word_left, word_right):
                            dp[word_right.index] = max(dp[word_right.index], 
                                    dp[word_left.index] + 1)
        return max(dp)


def test_1():
    words = ["a","b","ba","bca","bda","bdca"]
    assert Solution().longestStrChain(words) == 4


def test_2():
    words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    assert Solution().longestStrChain(words) == 5


def test_3():
    """WA"""
    words = ["a","b","ab","bac"]
    assert Solution().longestStrChain(words) == 2
