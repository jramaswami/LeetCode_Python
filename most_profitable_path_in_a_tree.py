"""
LeetCode
2467. Most Profitable Path in a Tree
February 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Turn into a graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Find out Bob's path.
        parent = dict()
        parent[bob] = -1
        queue = collections.deque()
        queue.append(bob)
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in parent:
                    parent[v] = u
                    queue.append(v)
        # Reconstruct Bob's path by time
        path = [0]
        while parent[path[-1]] >= 0:
            path.append(parent[path[-1]])
        bobs_path_by_time = {u: t for t, u in enumerate(reversed(path))}

        # Find optimal path for Alice
        queue = collections.deque()
        queue.append((0, 0, 0))
        visited = set()
        visited.add(0)
        soln = -pow(10,10)
        while queue:
            u, income, tick = queue.popleft()
            # Adjust income
            if u in bobs_path_by_time and bobs_path_by_time[u] < tick:
                income += 0
            elif u in bobs_path_by_time and bobs_path_by_time[u] == tick:
                income += (amount[u] // 2)
            else:
                income += amount[u]
            is_leaf = True
            for v in graph[u]:
                if v not in visited:
                    is_leaf = False
                    queue.append((v, income, tick+1))
                    visited.add(v)
            if is_leaf:
                soln = max(soln, income)
        return soln
