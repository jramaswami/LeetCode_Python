"""
LeetCode
3025. Find the Number of Ways to Place People I
September 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        def has_upper_left(x1, y1, x2, y2):
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            # Invariant x1 <= x2
            # Horizontal line is ok
            if x1 == x2:
                return True
            # Vertical line is ok
            if y1 == y2:
                return True
            # x1 is < x2, so y1 has to be more than y2
            return y1 > y2


        soln = 0
        # Invariant x1 <= x2
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i+1:], start=i+1):

                if not has_upper_left(x1, y1, x2, y2):
                    continue

                # Look for collision
                min_x, max_x = min(x1,x2), max(x1,x2)
                min_y, max_y = min(y1,y2), max(y1,y2)
                collision = False
                for k, (x3, y3) in enumerate(points):
                    if k == i or k == j:
                        continue

                    if (min_x <= x3 <= max_x) and (min_y <= y3 <= max_y):
                        collision = True
                        break

                if not collision:
                    soln += 1
        return soln