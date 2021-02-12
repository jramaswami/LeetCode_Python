"""
LeetCode ::  Number of Steps to Reduce a Number to Zero
jramaswami
"""
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1
            if num % 2:
                num -= 1
            else:
                num //= 2
        return count


def test_1():
    assert Solution().numberOfSteps(14) == 6

def test_2():
    assert Solution().numberOfSteps(8) == 4

def test_3():
    assert Solution().numberOfSteps(123) == 12
