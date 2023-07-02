"""
LeetCode
1601. Maximum Number of Achievable Transfer Requests
July 2023 Challenge
jramaswami

With a little help from Larry.
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

        def check(requests_bitmap):
            requests_delta = [0 for _ in range(n)]
            requests_fulfilled = 0
            for request_index in range(len(requests)):
                if (1 << request_index) & requests_bitmap:
                    requests_fulfilled += 1
                    move_from, move_to = requests[request_index]
                    requests_delta[move_from] -= 1
                    requests_delta[move_to] += 1
            if all(d == 0 for d in requests_delta):
                return requests_fulfilled
            return 0

        soln = 0
        for request_bitmap in range((1 << len(requests))):
            soln = max(soln, check(request_bitmap))
        return soln