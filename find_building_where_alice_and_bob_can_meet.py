"""
LeetCode
2940. Find Building Where Alice and Bob Can Meet
December 2024 Challenge
jramaswami

Thank You NeetCode.IO!
"""


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1 for _ in queries]
        groups = collections.defaultdict(list)
        for i, q in enumerate(queries):
            l, r = sorted(q)
            if l == r or heights[r] > heights[l]:
                result[i] = r
            else:
                h = max(heights[l], heights[r])
                groups[r].append((h, i))
        
        HT, QI = 0, 1
        queue = []
        for i, h in enumerate(heights):
            for qh, qi in groups[i]:
                heapq.heappush(queue, (qh, qi))
            while queue and h > queue[0][HT]:
                item = heapq.heappop(queue)
                result[item[QI]] = i
        
        return result
