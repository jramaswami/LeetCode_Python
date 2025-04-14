"""
LeetCode
1534. Count Good Triplets
April 2025 Challenge
jramaswami
"""


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        soln = 0
        for i, _ in enumerate(arr):
            for j, _ in enumerate(arr[i+1:], start=i+1):
                for k, _ in enumerate(arr[j+1:], start=j+1):
                    x = abs(arr[i] - arr[j])
                    y = abs(arr[j] - arr[k])
                    z = abs(arr[i] - arr[k])
                    if x <= a and y <= b and z <= c:
                        soln += 1
        return soln