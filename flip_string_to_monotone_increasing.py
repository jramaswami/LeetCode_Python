"""
LeetCode :: August 2021 Challenge :: Flip String to Monotone Increasing
jramaswami
"""


class Solution:
    def minFlipsMonoIncr(self, S):
        ones_prefix = [0 for _ in S]
        curr_ones = 0
        for i, c in enumerate(S):
            if c == '1':
                curr_ones += 1
            ones_prefix[i] = curr_ones

        curr_zeros = 0
        zeros_suffix = [0 for _ in S]
        for i, c in enumerate(reversed(S), start=1):
            j = len(S) - i
            if c == '0':
                curr_zeros += 1
            zeros_suffix[j] = curr_zeros

        # Start with changing all ones to zeros.
        soln = ones_prefix[-1]

        for i, _ in enumerate(S):
            ones_to_change = 0 if i == 0 else ones_prefix[i-1]
            zeros_to_change = zeros_suffix[i]
            soln = min(soln, ones_to_change + zeros_to_change)
        return soln


def test_1():
    S = "00110"
    assert Solution().minFlipsMonoIncr(S) == 1


def test_2():
    S = "010110"
    assert Solution().minFlipsMonoIncr(S) == 2


def test_3():
    S = "00011000"
    assert Solution().minFlipsMonoIncr(S) == 2
