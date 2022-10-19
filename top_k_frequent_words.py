"""
LeetCode :: October 2022 Challenge :: 692. Top K Frequent Words
jramaswami
"""


import collections
import heapq
from typing import *


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = collections.Counter(words)
        neg_freqs = [(-freq, word) for word, freq in freqs.items()]
        return [word for _, word in heapq.nsmallest(k, neg_freqs)]


def test_1():
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    expected = ["i","love"]
    assert Solution().topKFrequent(words, k) == expected


def test_2():
    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4
    expected = ["the","is","sunny","day"]
    assert Solution().topKFrequent(words, k) == expected