"""
LeetCode :: October 2021 Challenge :: 75. Sort Colors
jramaswami
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One pass, constant extra space.
        not_zero = 0
        not_two = len(nums) - 1

        i = 0
        while i < len(nums):

            # Update not_zero pointer.
            while not_zero < len(nums) and nums[not_zero] == 0:
                not_zero += 1

            # Update not_two pointer.
            while not_two >= 0 and nums[not_two] == 2:
                not_two -= 1

            if nums[i] == 0 and i > not_zero:
                # An out of position zero, swap it with the leftmost not zero.
                nums[not_zero], nums[i] = nums[i], nums[not_zero]
            elif nums[i] == 2 and i < not_two:
                # An out of position tow, swap it with the rightmost not two.
                nums[not_two], nums[i] = nums[i], nums[not_two]
            else:
                # This number is in place, move to the next one.
                i += 1
