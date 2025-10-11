"""
LeetCode
3186. Maximum Total Damage With Spell Casting
October 2025 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()

        def can_cast(curr, prev):
            if prev == None:
                return True

            if curr == prev:
                return True

            return not (prev-2 <= curr <= prev+2)

        @functools.cache
        def rec(i, prev):
            # Base case
            if i >= len(power):
                return 0

            # Do not cast this spell
            result = rec(i+1, prev)

            # Cast this spell
            if can_cast(power[i], prev):
                result = max(
                    result,
                    power[i] + rec(i+1, power[i])
                )
            return result

        return rec(0, None)