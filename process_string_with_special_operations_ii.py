"""
LeetCode
3614. Process String with Special Operations II
June 2026 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=lBlpxyJxsT8
"""


class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Compute length
        curr_len = 0
        for char in s:
            if char == '%':
                # Reverse (does not affect length)
                pass
            elif char == '#':
                # Double
                curr_len *= 2
            elif char == '*':
                if curr_len:
                    curr_len -= 1
            else:
                curr_len += 1

        # Check bounds
        if k >= curr_len:
            return '.'

        # Reverse engineer
        for char in reversed(s):
            if char == '%':
                # Adjust index for reversed array
                k = curr_len - 1 - k
            elif char == '#':
                # Undo double
                curr_len //= 2
                # Adjust index
                if k >= curr_len:
                    k -= curr_len
            elif char == '*':
                # Add character back in
                curr_len += 1
            else:
                # Add character
                if k == curr_len - 1:
                    return char
                curr_len -= 1