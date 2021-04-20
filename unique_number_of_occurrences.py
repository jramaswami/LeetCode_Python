"""
LeetCode :: 1207. Unique Number of Occurrences
jramaswami
"""
from typing import *
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ctr = Counter(arr)
        freqs = set(ctr.values())
        return len(ctr) == len(freqs)


def test_1():
    arr = [1,2,2,1,1,3]
    assert Solution().uniqueOccurrences(arr) == True

def test_2():
    arr = [1,2]
    assert Solution().uniqueOccurrences(arr) == False

def test_3():
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    assert Solution().uniqueOccurrences(arr) == True
