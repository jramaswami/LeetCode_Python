"""
LeetCode
2570. Merge Two 2D Arrays by Summing Values
March 2025 Challenge
jramaswami
"""


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ID, VAL = 0, 1
        i = j = 0
        soln = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i][ID] < nums2[j][ID]:
                soln.append(nums1[i])
                i += 1
            elif nums1[i][ID] > nums2[j][ID]:
                soln.append(nums2[j])
                j += 1
            elif nums1[i][ID] == nums2[j][ID]:
                item_id = nums1[i][ID]
                item_value = nums1[i][VAL] + nums2[j][VAL]
                soln.append([item_id, item_value])
                i += 1
                j += 1
        while i < len(nums1):
            soln.append(nums1[i])
            i += 1
        while j < len(nums2):
            soln.append(nums2[j])
            j += 1
        return soln
