"""
LeetCode
3097. Shortest Subarray With OR at Least K II
November 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def change_bits(x, delta, bits):
            for i in range(32):
                mask = 1 << i
                if x & mask:
                    bits[i] += delta

        def bits_to_number(bits):
            x = 0
            for i in range(32):
                if bits[i]:
                    mask = 1 << i
                    x |= mask
            return x
        
        INF = pow(10, 10)
        soln = INF
        window = collections.deque()
        bits = [0 for _ in range(32)]
        curr_value = 0
        for n in nums:
            window.append(n)
            change_bits(n, +1, bits)
            curr_value = bits_to_number(bits)
            while window and curr_value >= k:
                soln = min(soln, len(window))
                y = window.popleft()
                change_bits(y, -1, bits)
                curr_value = bits_to_number(bits)
        return -1 if soln == INF else soln
