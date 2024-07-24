"""
LeetCode
2191. Sort the Jumbled Numbers
July 2024 Challenge
jramaswami
"""


from typing import List


def map_number(n, mapping):
    t = 1
    m = 0
    while n:
        n, x = divmod(n, 10)
        y = mapping[x]
        m += (t * y)
        print(n, x, y, m)
        t *= 10
    return m


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        A = [(map_number(x, mapping), i, x) for i, x in enumerate(nums)]
        A.sort()
        return [t[-1] for t in A]


def test_map_number():
    mapping = [8,9,4,0,2,1,3,5,7,6]
    assert map_number(991, mapping) == 669
    assert map_number(338, mapping) == 7
    assert map_number(38, mapping) == 7


def test_1():
    mapping = [8,9,4,0,2,1,3,5,7,6]
    nums = [991,338,38]
    expected = [338,38,991]
    assert Solution().sortJumbled(mapping, nums) == expected


def test_2():
    mapping = [0,1,2,3,4,5,6,7,8,9]
    nums = [789,456,123]
    expected = [123,456,789]
    assert Solution().sortJumbled(mapping, nums) == expected


def test_3():
    "WA"
    mapping = [9,8,7,6,5,4,3,2,1,0]
    nums = [0,1,2,3,4,5,6,7,8,9]
    expected = [9,8,7,6,5,4,3,2,1,0]
    assert Solution().sortJumbled(mapping, nums) == expected