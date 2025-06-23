"""
LeetCode
2081. Sum of k-Mirror Numbers
June 2025 Challenge
jramaswami
"""


import itertools


def palindrome_generator(digits: int):
    if digits == 1:
        for x in range(1, 10):
            yield x
    elif digits == 2:
        for x in range(1, 10):
            yield int(f'{x}{x}')
    elif digits % 2 == 0:
        limit = pow(10, digits // 2)
        for x in range(limit // 10, limit):
            a = ''.join(str(x))
            b = a[::-1]
            yield int(a+b)
    else:
        limit = pow(10, digits // 2)
        limit = pow(10, digits // 2)
        for x in range(limit // 10, limit):
            a = ''.join(str(x))
            b = a[::-1]
            for y in range(10):
                yield int(f'{a}{y}{b}')


def convert_to_base(x: int, base: int) -> str:
    result = []
    while x:
        result.append(str(x % base))
        x //= base
    return ''.join(reversed(result))


def is_palindrome(t: str) -> bool:
    left = 0
    right = len(t) - 1
    while left <= right:
        if t[left] != t[right]:
            return False
        left += 1
        right -= 1
    return True


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        soln = 0
        digits = 1
        while n > 0:
            for x in palindrome_generator(digits):
                y = convert_to_base(x, k)
                if is_palindrome(y):
                    soln += x
                    n -= 1
                if n == 0:
                    break
            digits += 1
        return soln


def test_1():
    k = 2
    n = 5
    expected = 25
    assert Solution().kMirror(k, n) == expected


def test_2():
    k = 3
    n = 7
    expected = 499
    assert Solution().kMirror(k, n) == expected


def test_3():
    k = 7
    n = 17
    expected = 20379000
    assert Solution().kMirror(k, n) == expected