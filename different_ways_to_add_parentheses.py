"""
LeetCode
241. Different Ways to Add Parentheses
September 2024 Challenge
jramaswami
Thank You NeetCodeIO!
"""


import operator


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        OPS = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }

        def rec(left, right):
            res = []
            for i in range(left, right+1):
                if expression[i] in OPS:
                    nums1 = rec(left, i-1)
                    nums2 = rec(i+1,right)

                    for x in nums1:
                        for y in nums2:
                            res.append(OPS[expression[i]](x,y))
            if not res:
                res.append(int(expression[left:right+1]))
            return res

        return rec(0, len(expression)-1)
