"""
LeetCode :: May 2022 Challenge :: Maximum Product of Word Lengths
jramaswami
"""


class Solution:
    def maxProduct(self, words):
        soln = 0
        words0 = [set(w) for w in words]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not (words0[i] & words0[j]):
                    soln = max(soln, len(words[i]) * len(words[j]))
        return soln


def test_1():
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    expected = 16
    assert Solution().maxProduct(words) == expected


def test_2():
    words = ["a","ab","abc","d","cd","bcd","abcd"]
    expected = 4
    assert Solution().maxProduct(words) == expected


def test_3():
    words = ["a","aa","aaa","aaaa"]
    expected = 0
    assert Solution().maxProduct(words) == expected
