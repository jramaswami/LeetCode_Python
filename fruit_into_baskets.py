"""
LeetCode
904. Fruit Into Baskets
February 2023 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freqs = dict()
        window = collections.deque()
        count = 0
        soln = 0
        for f in fruits:
            # Add fruit to window.
            window.append(f)
            if f not in freqs:
                count += 1
                freqs[f] = 0
            freqs[f] += 1

            # While there are more than two kinds of fruit,
            # remove from left of window.
            while count > 2:
                x = window.popleft()
                freqs[x] -= 1
                if freqs[x] == 0:
                    count -= 1
            soln = max(soln, len(window))
        return soln


def test_1():
    fruits = [1,2,1]
    expected = 3
    assert Solution().totalFruit(fruits) == expected


def test_2():
    fruits = [0,1,2,2]
    expected = 3
    assert Solution().totalFruit(fruits) == expected


def test_3():
    fruits = [1,2,3,2,2]
    expected = 4
    assert Solution().totalFruit(fruits) == expected


def test_4():
    "WA"
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    expected = 5
    assert Solution().totalFruit(fruits) == expected
