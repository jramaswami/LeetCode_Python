"""
LeetCode :: October 2022 Challenge :: 1578. Minimum Time to Make Rope Colorful
jramaswami
"""


from typing import *
import heapq


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_color = None
        prev_times = []
        soln = 0
        for i, curr_color in enumerate(colors):
            if curr_color == prev_color:
                prev_times.append(neededTime[i])
            else:
                if len(prev_times) > 1:
                    soln += sum(heapq.nsmallest(len(prev_times) - 1, prev_times))
                prev_color = curr_color
                prev_times = [neededTime[i]]
        if len(prev_times) > 1:
            soln += sum(heapq.nsmallest(len(prev_times) - 1, prev_times))
        return soln


def test_1():
    colors = "abaac"
    neededTime = [1,2,3,4,5]
    expected = 3
    assert Solution().minCost(colors, neededTime) == expected


def test_2():
    colors = "abc"
    neededTime = [1,2,3]
    expected = 0
    assert Solution().minCost(colors, neededTime) == expected


def test_3():
    colors = "aabaa"
    neededTime = [1,2,3,4,1]
    expected = 2
    assert Solution().minCost(colors, neededTime) == expected