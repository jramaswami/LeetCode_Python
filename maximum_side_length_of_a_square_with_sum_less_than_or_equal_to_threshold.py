"""
LeetCode
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
January 2026 Challenge
jramaswami
"""


import collections
import itertools
from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefixes = [list(itertools.accumulate(row)) for row in mat]

        def get(row_index, left, right):
            if left == 0:
                return prefixes[row_index][right]
            return prefixes[row_index][right] - prefixes[row_index][left-1]

        def check(k):
            for left, _ in enumerate(mat[0]):
                right = left + k - 1 # inclusive
                if right >= len(mat[0]):
                    break
                curr_sum = 0
                window = collections.deque()
                for row_index, _ in enumerate(mat):
                    x = get(row_index, left, right)
                    curr_sum += x
                    window.append(x)
                    while len(window) > k:
                        curr_sum -= window.popleft()
                    if len(window) == k and curr_sum <= threshold:
                        return True
            return False

        low = 1
        high = len(mat[0])
        soln = 0
        while low <= high:
            mid = low + ((high - low) // 2)
            if check(mid):
                soln = max(soln, mid)
                low = mid + 1
            else:
                high = mid - 1
        return soln


def test_1():
    mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
    threshold = 4
    expected = 2
    assert Solution().maxSideLength(mat, threshold) == expected


def test_2():
    mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
    threshold = 1
    expected = 0
    assert Solution().maxSideLength(mat, threshold) == expected
