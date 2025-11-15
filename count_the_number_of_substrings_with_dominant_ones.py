"""
LeetCode
3234. Count the Number of Substrings With Dominant Ones
November 2025 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=QySHur5CGRI
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        next_zero = [N] * (N)
        for i in range(N-2, -1, -1):
            if s[i+1] == '0':
                next_zero[i] = i + 1
            else:
                next_zero[i] = next_zero[i+1]

        soln = 0
        for left in range(N):
            zeros = 1 if s[left] == '0' else 0
            right = left
            while zeros * zeros <= N:
                next_z = next_zero[right] if right < N else N
                ones = (next_z - left) - zeros
                if ones >= zeros * zeros:
                    soln += min(
                        next_z - right,
                        ones - (zeros*zeros) + 1
                    )
                right = next_z
                zeros += 1
                if right == N:
                    break

        return soln


def test_1():
    s = "00011"
    assert Solution().numberOfSubstrings(s) == 5


def test_2():
    s = "101101"
    assert Solution().numberOfSubstrings(s) == 16