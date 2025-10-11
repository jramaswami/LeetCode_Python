"""
LeetCode
3186. Maximum Total Damage With Spell Casting
October 2025 Challenge
jramaswami
"""


import functools
import collections
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freqs = collections.Counter(power)
        spells = list(sorted(freqs))

        def next_spell(i):
            # Has to be more than 2 greater than the previous spell
            j = i + 1
            while j < len(spells) and spells[j] <= spells[i] + 2:
                j += 1
            return j

        @functools.cache
        def rec(i):
            # Base case
            if i >= len(spells):
                return 0

            # Do not cast this spell
            result = rec(i+1)

            # Cast this spell
            damage = spells[i] * freqs[spells[i]]
            j = next_spell(i)
            result = max(
                result,
                damage + rec(j)
            )
            return result

        return rec(0)