"""
LeetCode
2698. Find the Punishment Number of an Integer
February 2025 Challenge
jramaswami
"""


def can_sum_to(x, n):
    """Return true if you can partition x into substrings that sum to n
    """

    x_str = str(x)

    def rec(i, acc):
        if i >= len(x_str):
            if acc == n:
                return True

        result = False
        for j in range(i+1, len(x_str)+1):
            t = int(x_str[i:j])
            result = result or rec(j, acc+t)
        return result
    
    return rec(0, 0)


class Solution:
    def punishmentNumber(self, n: int) -> int:
        soln = 0
        for i in range(1, n+1):
            if can_sum_to(i*i, i):
                soln += (i * i)
        return soln


def test_1():
    assert Solution().punishmentNumber(10) == 182


def test_2():
    assert Solution().punishmentNumber(37) == 1478
