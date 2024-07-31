"""
LeetCode
1105. Filling Bookcase Shelves
July 2024 Challenge
jramaswami
"""


import functools
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        @functools.cache
        def rec(i, w, h):
            if i >= len(books):
                return h

            # Start a new shelf
            result = h + rec(i + 1, books[i][0], books[i][1])
            # Stay on the same shelf
            if w + books[i][0] <= shelfWidth:
                w0 = w + books[i][0]
                h0 = max(h, books[i][1])
                result = min(
                    result,
                    rec(i + 1, w0, h0)
                )
            return result

        return rec(0, 0, 0)