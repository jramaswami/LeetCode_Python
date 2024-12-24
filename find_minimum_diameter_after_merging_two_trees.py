"""
LeetCode
3203. Find Minimum Diameter After Merging Two Trees
December 2024 Challenge
jramaswami
"""


import heapq


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        def build_graph(edges):
            graph = collections.defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph
        
        def get_diameter(cur, par, graph):
            max_d = 0
            max_child_paths = [0, 0]
            for nei in graph[cur]:
                if nei == par:
                    continue
                nei_d, nei_max_leaf_path = get_diameter(nei, cur, graph)
                max_d = max(max_d, nei_d)
                heapq.heappush(max_child_paths, nei_max_leaf_path)
                heapq.heappop(max_child_paths)
            max_d = max(max_d, sum(max_child_paths))
            return [max_d, 1 + max(max_child_paths)]

        graph1 = build_graph(edges1)
        graph2 = build_graph(edges2)

        d1, _ = get_diameter(0, -1, graph1)
        d2, _ = get_diameter(0, -1, graph2)

        return max(d1, d2, 1 + ceil(d1 / 2) + ceil(d2 / 2))
