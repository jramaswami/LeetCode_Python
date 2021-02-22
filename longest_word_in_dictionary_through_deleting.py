"""
LeetCode :: Longest Word in Dictionary through Deleting
jramaswami
"""
from typing import *


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        soln = ""
        for word in d:
            j = 0
            for i, c in enumerate(s):
                if j < len(word) and c == word[j]:
                    j += 1

            if j == len(word):
                if len(word) > len(soln):
                    soln = word
                elif len(word) == len(soln):
                    soln = min(word, soln)

        return soln


def test_1():
    s = "abpcplea"
    d = ["ale","apple","monkey","plea"]
    assert Solution().findLongestWord(s,d ) == "apple"

def test_2():
    s = "abpcplea"
    d = ["a","b","c"]
    assert Solution().findLongestWord(s,d ) == "a"

