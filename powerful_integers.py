"""
Leet Code :: April 2021 Challenge :: Powerful Integers
jramaswami
"""
from typing import *


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        soln = set()
        a = 1
        while a <= bound:
            b = 1
            while a + b <= bound:
                soln.add(a + b)
                if b * y == b:
                    break
                b *= y
            if a * x == a:
                break
            a *= x
        return list(soln)


def test_1():
    x = 3
    y = 5
    bound = 15
    expected = [2,4,6,8,10,14]
    assert sorted(Solution().powerfulIntegers(x, y, bound)) == expected


def test_2():
    x = 5
    y = 7
    bound = 1000
    expected = [32,2,132,968,6,8,74,12,626,174,368,632,50,468,54,674,344,26,348,126]
    assert sorted(Solution().powerfulIntegers(x, y, bound)) == sorted(expected)


def test_3():
    x = 17
    y = 45
    bound = 100000
    expected = [2,83566,4958,91414,91142,85546,2026,290,46,18,96038,83522,334,91126,6938,2042,4914,2314,62]
    assert sorted(Solution().powerfulIntegers(x, y, bound)) == sorted(expected)

def test_4():
    x = 17
    y = 45
    bound = 1
    expected = []
    assert sorted(Solution().powerfulIntegers(x, y, bound)) == sorted(expected)

def test_5():
    """TLE"""
    x = 2
    y = 1
    bound = 10
    expected = [9,2,3,5]
    assert sorted(Solution().powerfulIntegers(x, y, bound)) == sorted(expected)