"""
LeetCode :: October 2022 Challenge :: 1531. String Compression II
jramaswami
"""


import math
import functools


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def encoding_length(freq):
            if freq <= 1:
                return freq
            if freq < 10:
                return 2
            if freq < 100:
                return 3
            return 4

        @functools.cache
        def rec(i, prev_char, prev_freq, removals_left):
            if i >= len(s):
                return encoding_length(prev_freq)

            result = math.inf
            # Case 1: remove
            if removals_left > 0:
                result = min(
                    result,
                    rec(i+1, prev_char, prev_freq, removals_left-1)
                )
            if s[i] == prev_char:
                # Case 2: keep matching prev char.
                result = min(
                    result,
                    rec(i+1, prev_char, prev_freq+1, removals_left)
                )
            else:
                # Case 3: keep not matching prev char.
                result = min(
                    result,
                    encoding_length(prev_freq) + rec(i+1, s[i], 1, removals_left)
                )
            return result

        return rec(0, '#', 0, k)


def test_1():
    s = "aaabcccd"
    k = 2
    expected = 4
    assert Solution().getLengthOfOptimalCompression(s, k) == expected


def test_2():
    s = "aabbaa"
    k = 2
    expected = 2
    assert Solution().getLengthOfOptimalCompression(s, k) == expected

def test_3():
    s = "aaaaaaaaaaa"
    k = 0
    expected = 3
    assert Solution().getLengthOfOptimalCompression(s, k) == expected