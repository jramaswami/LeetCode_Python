"""
LeetCode :: Grind 75 :: First Bad Version
jramaswami
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n
        soln = n
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if isBadVersion(mid):
                soln = min(soln, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return soln
