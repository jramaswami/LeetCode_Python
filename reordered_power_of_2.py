"""
LeetCode :: August 2022 Challenge :: Reordered Power of 2
jramaswami
"""


def compute_digit_freqs(n):
    "Return frequency of each digit."
    freqs = [0 for _ in range(10)]
    while n:
        n, r = divmod(n, 10)
        freqs[r] += 1
    return tuple(freqs)


class Solution:
    def __init__(self):
        "Cache the frequency of digits in each power of 2."
        limit = pow(10, 9)
        n = 1
        self.cache = set()
        while n <= limit:
            self.cache.add(compute_digit_freqs(n))
            n *= 2

    def reorderedPowerOf2(self, N: int) -> bool:
        "Return True if you can reorder the digits of N into a power of 2."
        if compute_digit_freqs(N) in self.cache:
            return True
        return False



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
