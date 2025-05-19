"""
LeetCode
3024. Type of Triangle
May 2025
jramaswami
"""


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b , c = nums
        if (a + b) > c and (a + c) > b and (b + c) > a:
            if a == b and a == c and b == c:
                return "equilateral"
            if a == b or a == c or b == c:
                return "isosceles"
            return "scalene"
        return "none"