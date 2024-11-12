"""
LeetCode
2070. Most Beautiful Item for Each Query
November 2024 Challenge
jramaswami
"""


import heapq


PRICE, BEAUTY = 0, 1


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price
        items0 = list(items)
        items0.sort(reverse=True)
        # Sort queries
        queries0 = [(q, i) for i, q in enumerate(queries)]
        queries0.sort()

        soln = [0 for _ in queries0]
        # Use a Max Heap to keep track of most beautiful item less than current price
        heap = []

        # Go through queries popping form sorted items and adding to the queue all items <= query price
        for query_price, query_index in queries0:
            while items0 and items0[-1][PRICE] <= query_price:
                _, beauty = items0.pop()
                heapq.heappush(heap, -beauty)
            if heap:
                soln[query_index] = -heap[0]
        return soln
