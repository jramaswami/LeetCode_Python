"""
LeetCode
2064. Minimized Maximum of Products Distributed to Any Store
November 2024 Challenge
jramaswami
"""


import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def check(k):
            x = 0
            for q in quantities:
                x += math.ceil(q / k)
            if x <= n:
                return True
            return False


        lo = 1
        hi = max(quantities)
        soln = hi
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = min(soln, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return soln

