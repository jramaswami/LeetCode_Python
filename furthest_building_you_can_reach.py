"""
Leet Code :: April 2021 Challenge :: Furthest Building You Can Reach
jramaswami
"""
from typing import *


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        queue = [(bricks, ladders)]
        new_queue = []
        for i, _ in enumerate(heights[:-1]):
            delta = heights[i+1] - heights[i]
            if delta > 0:
                advance = False
                for b, l in queue:
                    if l > 0:
                        new_queue.append((b, l - 1))
                        advance = True
                    if b >= delta:
                        new_queue.append((b - delta, l))
                        advance = True
                queue, new_queue = new_queue, []
                if not advance:
                    return i
        return len(heights) - 1


def test_1():
    heights = [4,2,7,6,9,14,12]
    bricks = 5
    ladders = 1
    expected = 4
    assert Solution().furthestBuilding(heights, bricks, ladders) == expected


def test_2():
    heights = [4,12,2,7,3,18,20,3,19]
    bricks = 10
    ladders = 2
    expected = 7
    assert Solution().furthestBuilding(heights, bricks, ladders) == expected


def test_3():
    heights = [14,3,19,3]
    bricks = 17
    ladders = 0
    expected = 3
    assert Solution().furthestBuilding(heights, bricks, ladders) == expected


def test_4():
    """WA"""
    heights = [1,5,1,2,3,4,10000]
    bricks = 4
    ladders = 1
    expected = 5
    assert Solution().furthestBuilding(heights, bricks, ladders) == expected