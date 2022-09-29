"""
LeetCode :: September 2022 Challege :: Find K Closest Elements
jramaswami
"""


import heapq


class Item:

    def __init__(self, value, x):
        self.value = value
        self.x = x

    def __lt__(self, other):
        """
        An item is less than the other if:
            |a - x| < |b - x|, or
            |a - x| == |b - x| and a < b
        """
        if abs(self.value - self.x) == abs(other.value - self.x):
            return self.value < other.value
        return abs(self.value - self.x) < abs(other.value - self.x)


class Solution:
    def findClosestElements(self, arr, k, x):
        soln = heapq.nsmallest(k, (Item(a, x) for a in arr))
        return list(sorted(i.value for i in soln))



def test_1():
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    expected = [1,2,3,4]
    assert Solution().findClosestElements(arr, k, x) == expected


def test_2():
    arr = [1,2,3,4,5]
    k = 4
    x = -1
    expected = [1,2,3,4]
    assert Solution().findClosestElements(arr, k, x) == expected