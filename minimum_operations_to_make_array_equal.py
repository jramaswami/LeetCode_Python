"""
LeetCode :: April 2021 Challenge :: Minimum Operations to Make Array Equal
jramaswami
"""
class Solution:
    def minOperations(self, n: int) -> int:
        soln = 0
        left = 1
        right = (2 * (n - 1)) + 1
        while left < right:
            soln += ((right - left) // 2)
            left += 2
            right -= 2
        return soln


def test_1():
    assert Solution().minOperations(3) == 2

def test_2():
    assert Solution().minOperations(6) == 9

def test_3():
    assert Solution().minOperations(862) == 185761
