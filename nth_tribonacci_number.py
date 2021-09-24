"""
LeetCode :: September Challenge :: N-th Tribonacci Number
jramaswami

OEIS: A000073
"""

class Solution:

    def tribonacci(self, n):
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a


def test_1():
    assert Solution().tribonacci(4) == 4


def test_2():
    assert Solution().tribonacci(25) == 1389537


def test_3():
    assert Solution().tribonacci(0) == 0


def test_all():
    tribonacci_numbers = [0,0,1,1,2,4,7,13,24,44,81,149,274,504,927,1705,
                          3136,5768,10609,19513,35890,66012,121415,223317,
                          410744,755476,1389537,2555757,4700770,8646064,
                          15902591,29249425,53798080,98950096,181997601,
                          334745777,615693474,1132436852]
    solver = Solution()
    for i, tn in enumerate(tribonacci_numbers):
        solver.tribonacci(i) == tn
