"""
LeetCode
564. Find the Closest Palindrome
August 2024 Challenge
jramaswami
"""


import math
from typing import List


def convert_to_palindrome(t: List[int]) -> List[int]:
    x = list(t)
    left = 0
    right = len(x) - 1
    while left <= right:
        x[right] = x[left]
        right -= 1
        left += 1
    return x


def previous_palindrome(t: List[int]) -> List[int]:
    x = list(t)
    left = right = len(t) // 2
    if len(t) % 2 == 0:
        left = right - 1
    while left >= 0:
        if x[left] > 0:
            a = x[left] - 1
            x[left] = a
            x[right] = a
            return x
        x[left] = 9
        x[right] = 9
        left -= 1
        right += 1

    return None

def next_palindrome(t: List[int]) -> List[int]:
    x = list(t)
    left = right = len(t) // 2
    if len(t) % 2 == 0:
        left = right - 1

    while left >= 0:
        if x[left] < 9:
            a = x[left] + 1
            x[left] = a
            x[right] = a
            return x
        x[left] = 0
        x[right] = 0
        left -= 1
        right += 1

    # If we have reached here, we are going up 1 digit
    p = [0] * (len(t) + 1)
    p[0] = p[-1] = 1
    return p


def digits_to_int(t):
    if t:
        return int("".join(str(x) for x in t))
    return 0


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # Convert n to list of digits
        t = [int(x) for x in n]
        p0 = [9] * (len(t)-1)
        p = convert_to_palindrome(t)
        p1 = previous_palindrome(p)
        p2 = next_palindrome(p)
        print(p0, p, p1, p2)

        m = int(n)
        curr_min = m
        result = "0"
        for p_ in sorted(digits_to_int(a) for a in ([0], p0, p, p1, p2)):
            d = abs(p_ - m)
            if d > 0 and d < curr_min:
                result = str(p_)
                curr_min = d
        return result


def test_1():
    n = "123"
    expected = "121"
    assert Solution().nearestPalindromic(n) == expected


def test_2():
    n = "1"
    expected = "0"
    assert Solution().nearestPalindromic(n) == expected


def test_3():
    n = "3475"
    expected = "3443"
    assert Solution().nearestPalindromic(n) == expected


def test_4():
    n = "20002"
    expected = "19991"
    assert Solution().nearestPalindromic(n) == expected


def test_5():
    n = "8238475"
    expected = "8238328"
    assert Solution().nearestPalindromic(n) == expected


def test_6():
    n = "33"
    expected = "22"
    assert Solution().nearestPalindromic(n) == expected


def test_7():
    n = "99"
    expected = "101"
    assert Solution().nearestPalindromic(n) == expected


def test_8():
    n = "1837722381"
    expected = "1837667381"
    assert Solution().nearestPalindromic(n) == expected


def test_9():
    n = "10"
    expected = "9"
