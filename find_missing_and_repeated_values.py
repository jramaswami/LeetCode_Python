"""
LeetCode
2965. Find Missing and Repeated Values
March 2025 Challenge
jramaswami
"""



class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = -1
        missing = -1
        visited = set()
        for row in grid:
            for val in row:
                if val in visited:
                    repeated = val
                visited.add(val)
        n = len(grid)
        for x in range(1, (n * n)+1):
            if x not in visited:
                missing = x
        return [repeated, missing]
