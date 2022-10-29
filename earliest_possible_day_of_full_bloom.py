"""
LeetCode :: October 2022 Challenge :: 2136. Earliest Possible Day of Full Bloom
jramaswami
"""


from typing import *


class Solution:

    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        curr_planting_day = 0
        max_bloom_day = 0
        for g, p in sorted(zip(growTime, plantTime), reverse=True):
            max_bloom_day = max(max_bloom_day, curr_planting_day + p + g)
            curr_planting_day += p
        return max_bloom_day


def test_1():
    plantTime = [1,4,3]
    growTime = [2,3,1]
    expected = 9
    assert Solution().earliestFullBloom(plantTime, growTime) == expected


def test_2():
    plantTime = [1,2,3,2]
    growTime = [2,1,2,1]
    expected = 9
    assert Solution().earliestFullBloom(plantTime, growTime) == expected


def test_3():
    plantTime = [1]
    growTime = [1]
    expected = 2
    assert Solution().earliestFullBloom(plantTime, growTime) == expected