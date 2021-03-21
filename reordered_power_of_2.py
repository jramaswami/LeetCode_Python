"""
LeetCode :: March 2021 Challenge :: Reordered Power of 2
jramaswami
"""
class Solution:
    def __init__(self):
        # Initialize cache of powers of 2 by the number of digits.
        self.digits = [set() for _ in range(10)]
        p = 1
        while p <= pow(10, 9):
            s = str(p)
            index = len(s)
            key = "".join(sorted(s))
            self.digits[index].add(key)
            p *= 2

    def reorderedPowerOf2(self, N: int) -> bool:
        key = "".join(sorted(str(N)))
        return key in self.digits[len(key)]


def test_1():
    assert Solution().reorderedPowerOf2(1) == True

def test_2():
    assert Solution().reorderedPowerOf2(10) == False

def test_3():
    assert Solution().reorderedPowerOf2(16) == True

def test_4():
    assert Solution().reorderedPowerOf2(24) == False

def test_5():
    assert Solution().reorderedPowerOf2(46) == True
