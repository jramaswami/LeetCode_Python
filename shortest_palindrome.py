"""
LeetCode
214. Shortest Palindrome
September 2024 Challenge
jramaswami
Thank You NeetCodeIO!
"""


import functools


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "":
            return s
            
        @functools.cache
        def is_palindrome(left, right):
            if left >= right:
                return True

            return s[left] == s[right] and is_palindrome(left+1, right-1)
        
        for right in range(len(s)-1, -1, -1):
            if is_palindrome(0, right):
                t = s[right+1:][::-1]
                return t + s
