"""
LeetCode
66. Plus One
January 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        soln = []
        for i in range(len(digits)-1, -1, -1):
            carry, n = divmod(digits[i] + carry, 10)
            soln.append(n)
        if carry:
            soln.append(carry)
        return soln[::-1]