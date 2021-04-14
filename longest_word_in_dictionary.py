"""
LeetCode :: 720. Longest Word in Dictionary
jramaswami
"""
from typing import *
from collections import defaultdict


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Create a dictionary of prefixes.
        prefix_dict = defaultdict(list)
        queue = set()
        for word in words:
            prefix = word[:-1]
            prefix_dict[prefix].append(word)
            if len(word) == 1:
                queue.add(word)
        
        # BFS search to find the solution.
        soln = ""
        new_queue = set()
        while queue:
            for prefix in queue:
                if len(prefix) > len(soln):
                    soln = prefix
                elif len(prefix) == len(soln):
                    soln = min(soln, prefix)
                for word in prefix_dict[prefix]:
                    new_queue.add(word)
            queue, new_queue = new_queue, set()

        return soln


        
def test_1():
    words = ["w","wo","wor","worl","world"]
    assert Solution().longestWord(words) == "world"


def test_2():
    words = ["a","banana","app","appl","ap","apply","apple"]
    assert Solution().longestWord(words) == "apple"


def test_3():
    words = ["b", "ab", "abc", "abcd"]
    assert Solution().longestWord(words) == "b"


def test_4():
    words = ["ab", "abc", "abcd"]
    assert Solution().longestWord(words) == ""
