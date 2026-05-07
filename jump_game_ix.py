"""
LeetCode
3660. Jump Game IX
May 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        parent = list(range(len(nums)))
        size = [1 for _ in nums]
        comp_max = list(nums)

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                if size[a] < size[b]:
                    a,b  = b,a
                size[a] += size[b]
                comp_max[a] = max(comp_max[b], comp_max[a])
                parent[b] = a

        for i, n in enumerate(nums):
            # Backwards only allowed for smaller jumps
            for j, x in enumerate(nums[:i]):
                if x > n:
                    union(i, j)

        return [comp_max[find(i)] for i, _ in enumerate(nums)]


def test_1():
    nums = [2,3,1]
    expected = [3,3,3]
    assert Solution().maxValue(nums) == expected