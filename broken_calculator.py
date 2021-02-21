"""
LeetCode :: Broken Calculator
jramaswami

REF: https://www.geeksforgeeks.org/convert-number-m-n-using-minimum-number-given-operations/
"""
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X == Y:
            return 0
        elif X > Y:
            return X - Y
        else:
            if Y % 2:
                return 1 + self.brokenCalc(X, Y + 1)
            else:
                return 1 + self.brokenCalc(X, Y // 2)


def test_1():
    assert Solution().brokenCalc(2, 3) == 2

def test_2():
    assert Solution().brokenCalc(5, 8) == 2

def test_3():
    assert Solution().brokenCalc(3, 10) == 3

def test_4():
    assert Solution().brokenCalc(1024, 1) == 1023
