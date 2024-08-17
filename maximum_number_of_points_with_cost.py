"""
LeetCode
1937. Maximum Number of Points with Cost
August 2024 Challenge
jramaswami
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        prev_row = list(points[0])
        curr_row = [0 for _ in points[0]]
        for r, row in enumerate(points[1:], start=1):
            # Compute the most points from prev row moving left / right
            left = [0 for _ in row]
            for c in range(len(row)):
                if c == 0:
                    left[c] = prev_row[c]
                else:
                    left[c] = max(left[c-1]-1, prev_row[c])
            right = [0 for _ in row]
            for c in range(len(row)-1, -1, -1):
                if c == len(row) - 1:
                    right[c] = prev_row[c]
                else:
                    right[c] = max(right[c+1]-1, prev_row[c])
            
            for c in range(len(row)):
                curr_row[c] = points[r][c] + max(left[c], right[c])
        
            curr_row, prev_row = [0 for _ in points[0]], curr_row

        return max(prev_row)
