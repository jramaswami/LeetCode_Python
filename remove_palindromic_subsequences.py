"""
LeetCode :: June 2022 Challenge :: 1332. Remove Palindromic Subsequences
jramaswami
"""


class Solution:

    def removePalindromeSub(self, s: str) -> int:

        def is_palindrome(t: str) -> bool:
            left = 0
            right = len(t) - 1
            while left <= right:
                if t[left] != t[right]:
                    return False
                left += 1
                right -= 1
            return True

        return (1 if is_palindrome(s) else 2)
