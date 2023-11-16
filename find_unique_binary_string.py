"""
LeetCode
1980. Find Unique Binary String
November 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])

        T = list(nums)
        expected_len = pow(2, n)
        soln = []
        for i in range(n):
            expected_len //= 2
            zeros = []
            ones = []
            for x in T:
                if x[i] == '0':
                    zeros.append(x)
                else:
                    ones.append(x)

            if len(ones) < expected_len:
                T = ones
                soln.append("1")
            else:
                T = zeros
                soln.append("0")

        return ''.join(soln)


def test_1():
    nums = ["01","10"]
    result = Solution().findDifferentBinaryString(nums)
    assert result not in nums


def test_2():
    nums = ["00","01"]
    result = Solution().findDifferentBinaryString(nums)
    assert result not in nums


def test_3():
    nums = ["111","011","001"]
    result = Solution().findDifferentBinaryString(nums)
    assert result not in nums


import random


def test_a():
    for _ in range(100):
        remove = random.randint(0, pow(2, 16)-1)
        nums = [f'{x:016b}' for x in range(pow(2, 16)) if x != remove]
        result = Solution().findDifferentBinaryString(nums)
        assert result not in nums