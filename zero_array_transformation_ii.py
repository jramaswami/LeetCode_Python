"""
LeetCode
3356. Zero Array Transformation II
March 2025 Challenge
jramaswami
Thank You Larry!
"""


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        Q = len(queries)

        def check(t):
            diff = [0 for _ in range(N+1)]
            for l, r, v in queries[:t]:
                diff[l] += v
                diff[r+1] -= v
            
            curr = 0
            for i in range(N):
                curr += diff[i]
                if curr < nums[i]:
                    return False
            return True

        left = 0
        right = Q + 1
        while left  < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left if left <= Q else -1
