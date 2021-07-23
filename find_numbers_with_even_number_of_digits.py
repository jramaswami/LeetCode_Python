"""
LeetCode :: Arrays Module :: Find Numbers with Even Number of Digits
jramaswami
"""

class Solution:
    def findNumbers(self, nums):

        def count_digits(n):
            digits = 0
            while n:
                digits += 1
                n //= 10
            return digits

        return sum(count_digits(n) % 2 == 0 for n in nums)


def test_1():
    nums = [12,345,2,6,7896]
    assert Solution().findNumbers(nums) == 2


def test_2():
    nums = [555,901,482,1771]
    assert Solution().findNumbers(nums) == 1

def test_3():
    """WA"""
    nums = [1000]
    assert Solution().findNumbers(nums) == 1
