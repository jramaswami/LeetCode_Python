"""
LeetCode
945. Minimum Increment to Make Array Unique
jramaswami
"""


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        stack = [nums[0]]
        soln = 0
        for n in nums[1:]:
            if n <= stack[-1]:
                soln += (stack[-1] + 1 - n)
                stack.append(stack[-1]+1)
            else:
                stack.append(n)
        return soln
