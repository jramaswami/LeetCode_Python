"""
LeetCode
3003. Maximize the Number of Partitions After Operations
October 2025 Challenge
jramaswami

REF: algo.monster/liteproblems/3003
"""


import functools


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:

        @functools.cache
        def rec(index, curr_chars, can_change):
            # Base case
            if index >= len(s):
                return 1

            b = (ord(s[index]) - ord('a'))
            char_bit = 1 << b
            next_chars = curr_chars | char_bit

            if next_chars.bit_count() > k:
                result = 1 + rec(index+1, char_bit, can_change)
            else:
                result = rec(index+1, next_chars, can_change)

            if can_change:
                for c in range(26):
                    b = 1 << c
                    next_chars = curr_chars | b
                    if next_chars.bit_count() > k:
                        result = max(result, 1 + rec(index+1, b, 0))
                    else:
                        result = max(result, rec(index+1, next_chars, 0))

            return result

        return rec(0, 0, 1)
