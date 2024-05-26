"""
LeetCode
552. Student Attendance Record II
May 2024 Challenge
jramaswami
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        # Convert to prev/curr table
        # curr[absences][lates] where absences are 0, 1 and lates are 0, 1, 2
        prev = [[0 for _ in range(3)] for _ in range(2)]
        curr = [[0 for _ in range(3)] for _ in range(2)]
        prev[0][0] = 1

        for i in range(n):
            # Present day i
            # prev[a][l] -> curr[a][0]
            for a in range(2):
                for l in range(3):
                    curr[a][0] += prev[a][l]
                    curr[a][0] %= MOD

            # Absent day i
            # prev[0][l] -> curr[1][0]
            for l in range(3):
                curr[1][0] += prev[0][l]
                curr[1][0] %= MOD

            # Late day i
            # prev[a][l] -> curr[1][l+1] where l < 2
            for a in range(2):
                for l in range(2):
                    curr[a][l+1] += prev[a][l]
                    curr[a][l+1] %= MOD

            prev = curr
            curr = [[0 for _ in range(3)] for _ in range(2)]

        soln = 0
        for a in range(2):
            for l in range(3):
                soln += prev[a][l]
                soln %= MOD
        return soln % MOD


def test_1():
    assert Solution().checkRecord(2) == 8


def test_2():
    assert Solution().checkRecord(1) == 3


def test_3():
    assert Solution().checkRecord(10101) == 183236316


def test_4():
    "MLE"
    assert Solution().checkRecord(99995) == 969766675