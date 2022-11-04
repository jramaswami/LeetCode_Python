"""
LeetCode :: 345. Reverse Vowels of a String
November 2022 Challenge
jramaswami
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        t = list(s)
        left = 0
        right = len(t) - 1
        while left < right:
            while left < right and t[left] not in vowels:
                left += 1
            while left < right and t[right] not in vowels:
                right -= 1
            t[left], t[right] = t[right], t[left]
            left += 1
            right -= 1
        return "".join(t)


def test_1():
    s = "hello"
    expected = "holle"
    assert Solution().reverseVowels(s) == expected


def test_2():
    s = "leetcode"
    expected = "leotcede"
    assert Solution().reverseVowels(s) == expected