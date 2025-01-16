"""
LeetCode
2425. Bitwise XOR of All Pairings
January 2025 Challenge
jramaswami
"""



class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        soln = 0
        for b in range(32):
            mask = 1 << b
            set1 = set2 = 0
            
            for x in nums1:
                if mask & x:
                    set1 += 1
            
            for y in nums2:
                if mask & y:
                    set2 += 1
            
            unset1 = len(nums1) - set1
            unset2 = len(nums2) - set2

            total_set_bits = (set1 * unset2) + (set2 * unset1)
            if total_set_bits % 2:
                soln |= mask
        return soln
