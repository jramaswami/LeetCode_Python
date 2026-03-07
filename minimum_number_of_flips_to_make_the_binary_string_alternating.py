"""
LeetCode
1888. Minimum Number of Flips to Make the Binary String Alternating
March 2026 Challenge
jramaswami
"""


import collections


class Solution:
    def minFlips(self, s: str) -> int:
        def compute(start_ones, offset_ones, N):
            offset_length = N // 2
            start_length = offset_length + (N % 2)
            start_zeros = start_length - start_ones
            offset_zeros = offset_length - offset_ones
            x = start_zeros + offset_ones   # 1010...
            y = start_ones + offset_zeros   # 0101...
            return min(x, y)

        x = collections.deque(int(c) for c in s)
        start_ones = offset_ones = 0
        for i, n in enumerate(x):
            if i % 2:
                offset_ones += n
            else:
                start_ones += n
        N = len(x)
        soln = compute(start_ones, offset_ones, N)
        for _ in range(N):
            # Remove from start ones
            start_ones -= x[0]
            # Swap start and offset
            start_ones, offset_ones = offset_ones, start_ones
            # Rotate
            x.rotate(-1)
            # Add the moved value back in
            if (N-1) % 2:
                offset_ones += x[-1]
            else:
                start_ones += x[-1]
            soln = min(soln, compute(start_ones, offset_ones, N))
        return soln