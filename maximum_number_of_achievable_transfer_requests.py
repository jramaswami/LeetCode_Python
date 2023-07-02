"""
LeetCode
1601. Maximum Number of Achievable Transfer Requests
July 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        request_fulfilled = [False for _ in requests]
        # Covert requests in adjacency list where a node's list
        # contains the index of the request (edge).
        graph = [[] for _ in range(n)]
        for i, (u, v) in enumerate(requests):
            if u == v:
                request_fulfilled[i] = True
            else:
                graph[u].append(i)

        longest_cycle = []
        def dfs(node, path):
            nonlocal longest_cycle
            if path and requests[path[0]][0] == node:
                # Cycle found.
                if len(path) > len(longest_cycle):
                    longest_cycle = list(path)

            for request_index in graph[node]:
                if not request_fulfilled[request_index]:
                    path.append(request_index)
                    request_fulfilled[request_index] = True
                    dfs(requests[request_index][1], path)
                    path.pop()
                    request_fulfilled[request_index] = False

        for root in range(n):
            while 1:
                longest_cycle = []
                path = []
                dfs(root, path)
                if longest_cycle:
                    for request_index in longest_cycle:
                        request_fulfilled[request_index] = True
                else:
                    break

        return sum(request_fulfilled)