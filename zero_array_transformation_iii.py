"""
LeetCode
3362. Zero Array Transformation III
May 2025 Challenge
Thank You Larry!
"""


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        LEFT, RIGHT = 0, 1
        Q = collections.deque(sorted(queries))
        useable = []
        using = []
        count = 0
        for index, x in enumerate(nums):
            # Put the right index of any query that can be used
            # into the the heap of useable queries
            while Q and Q[0][LEFT] <= index:
                heapq.heappush(useable, -Q[0][RIGHT])
                Q.popleft()

            # Remove queries that we are no long using
            while using and using[0] < index:
                heapq.heappop(using)

            while len(using) < x:
                if not useable:
                    return -1
                right = -heapq.heappop(useable)
                if right >= index:
                    heapq.heappush(using, right)
                    count += 1
        return len(queries) - count