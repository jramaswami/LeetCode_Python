"""
LeetCode
9. Palindrome Number
jramaswami
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        def is_palindrome(t):
            left = 0
            right = len(t) - 1
            while left <= right:
                if t[left] != t[right]:
                    return False
                left += 1
                right -= 1
            return True

        def number_to_list(t):
            digits = []
            while t:
                t, r = divmod(t, 10)
                digits.append(r)
            return digits

        # A negative number is never a palindrome
        if x < 0:
            return False

        return is_palindrome(number_to_list(x))


def test_1():
    x = 121
    expected = True
    assert Solution().isPalindrome(x) == expected


def test_2():
    x = 121
    expected = True
    assert Solution().isPalindrome(x) == expected


def test_3():
    x = 121
    expected = True
    assert Solution().isPalindrome(x) == expected