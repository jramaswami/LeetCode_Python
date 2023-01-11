"""
LeetCode
1443. Minimum Time to Collect All Apples in a Tree
January 2023 Challenge
jramaswami
"""


class Solution(object):
    def minTime(self, n, edges, hasApple):
        graph = [[] for _ in hasApple]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def traverse(u, p):
            t = 0
            for v in graph[u]:
                if v != p:
                    t += traverse(v, u)

            if t > 0 or hasApple[u]:
                return t + 2
            return 0

        return sum(traverse(v, 0) for v in graph[0])