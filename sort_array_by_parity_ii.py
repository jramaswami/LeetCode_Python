"""
LeetCode :: September 2021 Challenge ::  Sort Array By Parity II
jramaswami
"""


class Solution:

    def sortArrayByParityII(self, nums):

        i = -1
        j = -2
        while 1:
            # Find the first number that is even parity and odd index
            while 1:
                i += 2
                if i >= len(nums) or nums[i] % 2 == 0:
                    break
            # Find the first number that is odd parity and even index
            while 1:
                j += 2
                if j >= len(nums) or nums[j] % 2 == 1:
                    break

            if i >= len(nums) or j >= len(nums):
                return nums

            # Swap
            nums[i], nums[j] = nums[j], nums[i]


def check(nums):
    """Check solution."""
    assert (i % 2 == n % 2 for i, n in enumerate(nums))


def test_1():
    nums = [4,2,5,7]
    result = Solution().sortArrayByParityII(nums)
    check(result)


def test_2():
    nums = [2,3]
    result = Solution().sortArrayByParityII(nums)
    check(result)


def test_random():
    import random
    for _ in range(100):
        N = 2 * random.randint(1, pow(10, 4))
        nums = list(range(N))
        random.shuffle(nums)
        result = Solution().sortArrayByParityII(nums)
        check(result)
