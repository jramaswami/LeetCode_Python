"""
LeetCode :: November 2021 Challenge :: 260. Single Number III
"""


import functools
import operator


class Solution:
    def singleNumber(self, nums):

        def lsb_mask(n):
            mask = 1
            while not n & mask:
                print(mask)
                mask = mask << 1
                if mask > pow(2, 32):
                    break
            return mask

        # XOR all the numbers giving X such that X = a ^ b.
        X = functools.reduce(operator.xor, nums)
        # Since a != b any set bit in X is unique to one of the numbers.
        # Find that bit.
        L = lsb_mask(X)
        # If we XOR all the numbers with the unique bit set, the result
        # will be a, since that bit is not set in b and all other numbers
        # appear twice and will cancel out.
        a = functools.reduce(operator.xor, [n for n in nums if n & L])
        # Once we know a, we can get be by XORing X and a.
        b = X ^ a
        return [a, b]


def test_1():
    nums = [1,2,1,3,2,5]
    expected = [3, 5]
    assert set(Solution().singleNumber(nums)) == set(expected)


def test_2():
    nums = list(range(1, 100)) * 2
    nums.extend([-1, -100])
    expected = [-1, -100]
    print(nums)
    assert set(Solution().singleNumber(nums)) == set(expected)
