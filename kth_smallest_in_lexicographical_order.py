"""
LeetCode
440. K-th Smallest in Lexicographical Order
September 2024 Challenge
jramaswami
Thank You NeetCodeIO!
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count(curr):
            result = 0
            neighbor = curr + 1
            while curr <= n:
                result += min(neighbor, n+1) - curr
                curr *= 10
                neighbor *= 10
            return result

        curr = 1
        i = 1
        while i < k:
            steps = count(curr)
            if i + steps <= k:
                curr += 1
                i += steps
            else:
                curr *= 10
                i += 1

        return curr
