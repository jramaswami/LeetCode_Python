"""
LeetCode
514. Freedom Trail
April 2024 Challenge
jramaswami
"""


import collections
import math


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        def distance(i, j):
            "Return the distance between i and j in the ring"
            if i > j:
                i, j = j, i
            d1 = j - i
            d2 = i + len(ring) - j
            return min(d1, d2)

        locations = collections.defaultdict(list)
        for i, x in enumerate(ring):
            locations[x].append(i)

        # dp[key index][ring index] = min distance
        dp = [[math.inf for _ in ring] for _ in key]
        for ring_index in locations[key[0]]:
            distance_to_next_value = distance(0, ring_index)
            dp[0][ring_index] = min(dp[0][ring_index], distance_to_next_value)

        for key_index in range(0, len(key) - 1):
            curr_key_value = key[key_index]
            next_key_value = key[key_index+1]
            for from_ring_index in locations[curr_key_value]:
                curr_distance = dp[key_index][from_ring_index]
                for to_ring_index in locations[next_key_value]:
                    distance_to_next_value = distance(from_ring_index, to_ring_index)
                    dp[key_index+1][to_ring_index] = min(
                        dp[key_index+1][to_ring_index],
                        curr_distance + distance_to_next_value
                    )
        return min(dp[-1]) + len(key)


def test_1():
    ring = "godding"
    key = "gd"
    expected = 4
    result = Solution().findRotateSteps(ring, key)
    assert result == expected


def test_2():
    ring = "godding"
    key = ring
    expected = 13
    result = Solution().findRotateSteps(ring, key)
    assert result == expected


def test_1():
    ring = "godding"
    key = "gd"
    expected = 4
    result = Solution().findRotateSteps(ring, key)
    assert result == expected


def test_3():
    "TLE"
    ring = "caotmcaataijjxi"
    key = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
    expected = 137
    result = Solution().findRotateSteps(ring, key)
    assert result == expected