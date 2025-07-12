"""
LeetCode
1900. The Earliest and Latest Rounds Where Players Compete
July 2025 Challenge
jramaswami
"""


import functools
import math
from typing import List


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @functools.cache
        def get_next_states(f, s, k):
            next_states = set()
            for win_lose in range(0, pow(2, k // 2)):
                winners = set()
                if k % 2:
                    winners.add(k // 2)
                for i in range(k // 2):
                    mask = 1 << i
                    is_winner = (win_lose & mask)
                    if is_winner:
                        winners.add(i)
                    else:
                        winners.add(k - i - 1)
                if f in winners and s in winners:
                    next_states.add(tuple(sorted(winners)))
            return next_states

        def is_end_state(f, s, k):
            return s == k - f - 1

        @functools.cache
        def rec(i, f, s, k, fn):
            # print(f'rec({i=}, {f=}, {s=}, {k=}, {fn=}) {is_end_state(f, s, k)=}')
            # Given k players left, determine all the possible positions
            # that f and s can take
            if is_end_state(f, s, k):
                return i

            result = math.inf if fn == min else -math.inf
            for next_state in get_next_states(f, s, k):
                f0 = next_state.index(f)
                s0 = next_state.index(s)
                k0 = len(next_state)
                result = fn(result, rec(i+1, f0, s0, k0, fn))
            return result

        a = rec(1, firstPlayer-1, secondPlayer-1, n, min)
        b = rec(1, firstPlayer-1, secondPlayer-1, n, max)
        return [a, b]


def test_1():
    n = 11
    firstPlayer = 2
    secondPlayer = 4
    expected = [3,4]
    assert Solution().earliestAndLatest(n, firstPlayer, secondPlayer) == expected