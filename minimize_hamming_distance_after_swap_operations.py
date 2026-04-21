"""
LeetCode
1722. Minimize Hamming Distance After Swap Operations
April 2026 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in allowedSwaps:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False for _ in source]

        same = 0
        for root, _ in enumerate(source):
            if not visited[root]:
                source_freqs = collections.Counter()
                target_freqs = collections.Counter()
                queue = collections.deque()
                queue.append(root)
                visited[root] = True
                while queue:
                    u = queue.popleft()
                    source_freqs[source[u]] += 1
                    target_freqs[target[u]] += 1
                    for v in graph[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)

                for x in source_freqs:
                    same += min(source_freqs[x], target_freqs[x])
        return len(source) - same