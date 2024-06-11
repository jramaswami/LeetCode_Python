"""
LeetCode
1122. Relative Sort Array
June 2024 Challenge
jramaswami
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        INF = pow(10,6)
        rel = {k: v for v, k in enumerate(arr2)}
        arr1.sort(key = lambda x: (rel[x], x) if x in rel else (INF, x))
        return arr1
