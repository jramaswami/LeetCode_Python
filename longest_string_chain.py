"""
LeetCode :: June 2022 Challenge :: Longest String Chain
jramaswami
"""


import collections
import itertools


class Solution:
    def longestStrChain(self, words):

        def is_predecessor(u, v):
            if len(words[u]) + 1 == len(words[v]):
                for i, (a, b) in enumerate(itertools.zip_longest(words[u], words[v], fillvalue=' ')):
                    if a != b:
                        return words[u][i:] == words[v][i+1:]
            return False


        words_by_length = collections.defaultdict(list)
        for i, word in enumerate(words):
            words_by_length[len(word)].append(i)

        predecessors = [1 for _ in words]

        for length in sorted(words_by_length.keys()):
            if length + 1 in words_by_length:
                for u in words_by_length[length]:
                    for v in words_by_length[length+1]:
                        if is_predecessor(u, v):
                            predecessors[v] = max(predecessors[v], 1 + predecessors[u])
        return max(predecessors)



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


def test_4():
    words = ["abcd","dbqca"]
    assert Solution().longestStrChain(words) == 1


def test_5():
    words = ["a","b","bx","bac"]
    assert Solution().longestStrChain(words) == 2
