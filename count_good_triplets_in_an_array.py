"""
LeetCode
2179. Count Good Triplets in an Array
April 2025 Challenge
jramaswami

Thank You Larry!
"""


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        mapping = {x: i for i, x in enumerate(nums1)}
        soln = 0
        visited = SortedList()
        nums2_ = [mapping[x] for x in nums2]
        for x in nums2_:
            left = len(visited)
            smaller_left = visited.bisect_left(x)
            bigger = N - 1 - x
            bigger_left = left - smaller_left
            bigger_right = bigger - bigger_left
            soln += (smaller_left * bigger_right)
            visited.add(x)
        return soln