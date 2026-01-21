"""
LeetCode
3314. Construct the Minimum Bitwise Array II
January 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def f(x):
            if x % 2 == 0:
                return -1

            for bit in range(32, -1, -1):
                mask = 1 << bit
                if mask & x:
                    y = x & (~mask)
                    if (y | y + 1) == x:
                        return y

        return [f(x) for x in nums]


def test_3():
    nums = [884532611,741533369,868936609,816315823,150570781,346594697,334726181,921762641,89355881,403165729,931242733]
    expected = [884532609,741533368,868936608,816315815,150570780,346594696,334726180,921762640,89355880,403165728,931242732]
    result = Solution().minBitwiseArray(nums)
    print(result)
    assert result == expected


if __name__ == '__main__':
    nums = list(range(1, 100, 2))
    def f(x):
            for n in range(0, x):
                if n | (n+1) == x:
                    return n
            return -1


    soln = [f(x) for x in nums]
    for n, x in zip(nums, soln):
        print(n, x, bin(n), bin(x))
