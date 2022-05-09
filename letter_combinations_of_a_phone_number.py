"""
LeetCode :: May 2022 Challenge :: 17. Letter Combinations of a Phone Number
jramaswami
"""


import itertools


LETTER_MAP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return ["".join(p) for p in itertools.product(*[LETTER_MAP[int(i)] for i in digits])]