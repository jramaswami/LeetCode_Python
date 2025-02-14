"""
LeetCode
1352. Product of the Last K Numbers
February 2025 Challenge
jramaswami
"""


class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]       

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
        else:
            x = self.nums[-1] * num
            self.nums.append(x)
        
    def getProduct(self, k: int) -> int:
        # If k > cache return zero
        if k >= len(self.nums):
            return 0
        i = len(self.nums) - k - 1
        return self.nums[-1] // self.nums[i]
