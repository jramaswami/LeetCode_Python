"""
LeetCode
1304. Find N Unique Integers Sum up to Zero
September 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        soln = []
        while n:
            if n == 1:
                soln.append(0)
                n -= 1
            else:
                soln.append(n)
                soln.append(-n)
                n -= 2
        return soln
