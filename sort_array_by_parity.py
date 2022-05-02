"""
LeetCode :: May 2022 Challenge :: Sort Array by Parity
jramaswami
"""


class Solution:
    def sortArrayByParity(self, nums):
        return sorted(nums, key=(lambda n: (n % 2, n)))


#
# Testing
#


def first_odd(A):
    for i, n in enumerate(A):
        if n % 2:
            return i
    return len(A)


def valid(A):
    p = first_odd(A)
    return all(n % 2 == 0 for n in A[:p]) and all(n % 2 == 1 for n in A[p:])


def test_1():
    nums = [3, 1, 2, 4]
    result = Solution().sortArrayByParity(nums)
    assert valid(result)


def test_random():
    import random
    for _ in range(100):
        N = pow(10, 4)
        A = [random.randint(0, 5000) for _ in range(N)]
        result = Solution().sortArrayByParity(A)
        assert valid(result)


def test_2():
    """RTE"""
    nums = [0]
    result = Solution().sortArrayByParity(nums)
    assert valid(result)
