"""
LeetCode
443. String Compression
March 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def compress(self, chars: List[str]) -> int:
        write_ptr = 0
        read_ptr = 1
        curr_freq = 1
        while read_ptr < len(chars):
            # Invariant: write_ptr is pointing to the current character.\
            if chars[read_ptr] != chars[write_ptr]:
                # Move off of current letter.
                write_ptr += 1
                if curr_freq > 1:
                    # Write the curr_freq
                    s = str(curr_freq)
                    for t in s:
                        chars[write_ptr] = t
                        write_ptr += 1
                # Write the new character
                chars[write_ptr] = chars[read_ptr]
                curr_freq = 1
            else:
                curr_freq += 1
            read_ptr += 1

        # Write final letter.
        # Move off of current letter.
        write_ptr += 1
        if curr_freq > 1:
            # Write the curr_freq
            s = str(curr_freq)
            for t in s:
                chars[write_ptr] = t
                write_ptr += 1
        return write_ptr


def test_1():
    chars = ["a","a","b","b","c","c","c"]
    expected = 6
    result = Solution().compress(chars)
    assert  result == expected
    assert "".join(chars[:result]) == "a2b2c3"


def test_2():
    chars = ["a"]
    expected = 1
    result = Solution().compress(chars)
    assert  result == expected
    assert "".join(chars[:result]) == "a"


def test_3():
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    expected = 4
    result = Solution().compress(chars)
    assert  result == expected
    assert "".join(chars[:result]) == "ab12"