"""
LeetCode
2197. Replace Non-Coprime Numbers in Array
September 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/2197
"""


import math
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums:
            stack.append(n)

            while len(stack) > 1:
                b, a = stack[-2:]
                g = math.gcd(a, b) 
                if g == 1:
                    break
                stack.pop()
                stack[-1] = (a * b) // g
        
        return stack
