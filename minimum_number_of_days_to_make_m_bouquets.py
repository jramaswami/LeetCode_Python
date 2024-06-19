"""
LeetCode
1482. Minimum Number of Days to Make m Bouquets
June 2024 Challenge
jramaswami
"""


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def check(d, m, k):
            blooms = 0
            bouquets = 0
            for n in bloomDay:
                if n <= d:
                    blooms += 1
                else:
                    blooms = 0
                
                if blooms == k:
                    blooms = 0
                    bouquets += 1
            return bouquets >= m
        
        INF = pow(10, 10)
        lo = 0
        hi = max(bloomDay)
        soln = INF
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            result = check(mid, m, k)
            if result:
                soln = min(soln, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        
        if soln < INF:
            return soln
        return -1
