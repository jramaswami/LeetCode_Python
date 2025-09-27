"""
LeetCode
812. Largest Triangle Area
September 2025 Challenge
jramawami
"""


import itertools


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        soln = 0
        for ps in itertools.combinations(points, 3):
            #                        N
            # Shoelace formula: 1/2 |S (x[i+1]+x[i])(y[i+1]-y[i])|
            #                        i=1
            summation = 0
            for i, _ in enumerate(ps):
                # x[i+1] + x[i]
                p = ps[(i+1)%3][0] + ps[i][0]
                # y[i+1] + y[i]
                q = ps[(i+1)%3][1] - ps[i][1]
                summation += (p*q)
            soln = max(soln, abs(summation) * 0.5)
        return soln