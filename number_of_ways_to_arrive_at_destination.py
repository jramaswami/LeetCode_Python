"""
LeetCode
1976. Number of Ways to Arrive at Destination
March 2025 Challenge
jramaswami
"""


from typing import List
import collections
import dataclasses
import heapq
import math


@dataclasses.dataclass(frozen=True)
class Edge:
    u: int
    v: int
    weight: int

    def other(self, a):
        if a == self.u:
            return self.v
        return self.u


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            e = Edge(u, v, w)
            graph[u].append(e)
            graph[v].append(e)

        dist = [math.inf for _ in range(n)]
        dist[0] = 0

        # ways_to_reach[node][distance]
        ways_to_reach = collections.defaultdict(lambda: collections.defaultdict(int))
        ways_to_reach[0][0] = 1
        visited = collections.defaultdict(lambda: collections.defaultdict(bool))
        MOD = pow(10, 9) + 7
        min_distance = math.inf
        queue = [(0, 0)]
        while queue:
            d, u = heapq.heappop(queue)
            if u == n-1:
                min_distance = min(min_distance, d)
            if d <= min_distance and not visited[u][d]:
                visited[u][d] = True
                for e in graph[u]:
                    v = e.other(u)
                    d0 = d + e.weight
                    ways_to_reach[v][d0] += ways_to_reach[u][d]
                    ways_to_reach[v][d0] %= MOD
                    heapq.heappush(queue, (d0, v))
        return ways_to_reach[n-1][min_distance] % MOD


def test_1():
    n = 7
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    expected = 4
    assert Solution().countPaths(n, roads) == expected


def test_3():
    """TLE"""
    n = 23
    roads = [[1,0,3229],[0,2,3925],[0,3,11879],[1,3,8650],[2,3,7954],[0,4,5751],[5,0,13299],[1,5,10070],[2,5,9374],[6,0,3516],[7,6,8438],[2,7,8029],[4,7,6203],[0,7,11954],[8,6,18080],[2,8,17671],[8,1,18367],[3,8,9717],[6,9,20566],[7,9,12128],[1,9,20853],[9,4,18331],[8,9,2486],[5,9,10783],[0,9,24082],[9,2,20157],[9,3,12203],[4,10,1614],[1,10,4136],[6,11,10060],[7,11,1622],[11,10,6211],[12,8,4751],[2,12,22422],[12,9,2265],[4,12,20596],[3,12,14468],[12,5,13048],[13,8,8243],[10,14,4407],[14,0,11772],[4,15,27067],[15,8,11222],[5,15,19519],[15,1,29589],[15,11,19242],[9,15,8736],[14,15,21046],[7,15,20864],[6,15,29302],[2,16,32501],[16,1,33197],[15,16,3608],[16,6,32910],[16,12,10079],[14,16,24654],[13,16,6587],[8,16,14830],[3,16,24547],[16,5,23127],[16,7,24472],[9,16,12344],[16,4,30675],[16,11,22850],[0,16,36426],[16,10,29061],[17,6,37406],[17,5,27623],[15,17,8104],[17,10,33557],[12,17,14575],[14,17,29150],[17,9,16840],[11,17,27346],[4,17,35171],[1,17,37693],[17,0,40922],[16,18,13938],[12,18,24017],[18,1,47135],[18,6,46848],[7,18,38410],[18,10,42999],[0,18,50364],[18,8,28768],[14,18,38592],[18,2,46439],[13,18,20525],[17,18,9442],[19,0,4751],[20,18,311],[20,1,47446],[11,20,37099],[15,20,17857],[20,16,14249],[8,20,29079],[14,20,38903],[20,3,38796],[13,20,20836],[20,4,44924],[0,20,50675],[12,20,24328],[6,20,47159],[20,9,26593],[20,17,9753],[7,20,38721],[20,5,37376],[20,2,46750],[18,21,7342],[21,15,24888],[1,21,54477],[21,20,7031],[21,9,33624],[21,12,31359],[21,19,52955],[13,21,27867],[10,21,50341],[21,8,36110],[21,5,44407],[21,2,53781],[11,21,44130],[0,21,57706],[21,3,45827],[6,21,54190],[21,4,51955],[17,21,16784],[22,15,26564],[22,18,9018],[22,2,55457],[7,22,47428],[4,22,53631],[21,22,1676]]
    expected = 1687
    assert Solution().countPaths(n, roads) == expected