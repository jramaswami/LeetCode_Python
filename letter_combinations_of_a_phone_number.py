"""
LeetCode :: April 2021 Challenge :: Letter Combinations of a Phone Number
jramaswami
"""
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                   '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        curr_soln = [tuple()]
        next_soln = []
        for digit in digits:
            for letter in letters[digit]:
                for soln in curr_soln:
                    soln0 = list(soln)
                    soln0.append(letter)
                    next_soln.append(tuple(soln0))
            curr_soln, next_soln = next_soln, []
        
        return sorted("".join(t) for t in curr_soln)
                    

def test_1():
    assert Solution().letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def test_2():
    assert Solution().letterCombinations("") == []

def test_3():
    assert Solution().letterCombinations("2") == ["a","b","c"]
