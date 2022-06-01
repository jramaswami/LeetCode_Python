"""
LeetCode :: Grind 75 :: Valid Palindrome
jramaswami
"""


class Solution:

    def isPalindrome(self, S):
        T = [c.lower() for c in S if c.isalpha()]
        left = 0
        right = len(T) - 1
        while left <= right:
            if T[left] != T[right]:
                return False
            left += 1
            right -= 1
        return True


def test_1():
    s = "A man, a plan, a canal: Panama"
    expected = True
    assert Solution().isPalindrome(s) == expected


def test_2():
    s = "race a car"
    expected = False
    assert Solution().isPalindrome(s) == expected


def test_3():
    s = " "
    expected = True
    assert Solution().isPalindrome(s) == expected


def test_4():
    "WA"
    s = "0P"
    expected = False
    assert Solution().isPalindrome(s) == expected
