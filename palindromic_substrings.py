"""
LeetCode :: March 2021 Challenge :: Palindromic Substrings
jramaswami
"""
from functools import lru_cache
import sys
sys.setrecursionlimit(1000000000)


@lru_cache(maxsize=None)
def is_palindromic_substring(start_index, end_index, string):
    if start_index == end_index:
        return True
    elif end_index - start_index == 1:
        return string[start_index] == string[end_index]
    else:
        # An substring is a palindrome if the start and end chars are the 
        # same and the substring between them is a palindrome.
        return (string[start_index] == string[end_index] and 
                is_palindromic_substring(start_index + 1, end_index - 1, string)
        )


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for start_index, _ in enumerate(s):
            for end_index, _ in enumerate(s[start_index:], start=start_index):
                if is_palindromic_substring(start_index, end_index, s):
                    count += 1
        return count
        

def test_1():
    assert Solution().countSubstrings("abc") == 3

def test_2():
    assert Solution().countSubstrings("aaa") == 6

def test_3():
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert Solution().countSubstrings(s) == 500500
