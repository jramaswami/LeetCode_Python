"""
LeetCode
1203. Sort Items by Groups Respecting Dependencies
August 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def sortItems(self, itemCount: int, groupCount: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Assign each of the -1 groups a unique group number
        for i, g in enumerate(group):
            if g == -1:
                group[i] = groupCount
                groupCount += 1

        # Topologically sort by group
        # Get dependencies between groups
        groupIndegree = [0 for _ in range(groupCount)]
        groupEdges = [set() for _ in range(groupCount)]
        groupEdgeCount = 0
        for i, bis in enumerate(beforeItems):
            iGroup = group[i]
            for bi in bis:
                biGroup = group[bi]
                print(f'{i=} {group[i]=} {bi=} {group[bi]=}')
                if iGroup != biGroup:
                    # biGroup must come before iGroup
                    groupIndegree[iGroup] += 1
                    groupEdges[biGroup].add(iGroup)
                    groupEdgeCount += 1
        print(f"{groupIndegree=}\n{groupEdges=}\n{groupEdgeCount=}")
        # Kahn's algorithm
        queue = collections.deque([i for i, d in enumerate(groupIndegree) if d == 0])
        groupTopo = []
        while queue:
            u = queue.popleft()
            groupTopo.append(u)
            for v in groupEdges[u]:
                groupIndegree[v] -= 1
                groupEdgeCount -= 1
                if groupIndegree[v] == 0:
                    queue.append(v)
        if groupEdgeCount:
            print('Unable to topo sort groups')
            return []

        print(f'{groupTopo=}')

        soln = []
        # Toplogically sort each group
        # Determine groups membership and indegree
        groupItems = [[] for _ in range(groupCount)]
        for i, g in enumerate(group):
            groupItems[g].append(i)

        # Get intergroup indegree
        itemIndegree = [0 for _ in group]
        itemEdges = [[] for _ in group]
        groupEdgeCount = [0 for _ in range(groupCount)]
        for i, bis in enumerate(beforeItems):
            for bi in bis:
                print(f'{i=} {group[i]=} {bi=} {group[bi]=}')
                if group[i] == group[bi]:
                    itemIndegree[i] += 1
                    itemEdges[bi].append(i)
                    groupEdgeCount[group[bi]] += 1

        for gi in groupTopo:
            print('topo sort of', gi, groupItems[gi])
            print('edges', [(i, itemEdges[i]) for i in groupItems[gi]])
            print('indegree', [(i, itemIndegree[i]) for i in groupItems[gi]])
            queue = collections.deque([i for i in groupItems[gi] if itemIndegree[i] == 0])
            print('queue', queue)
            while queue:
                u = queue.popleft()
                soln.append(u)
                for v in itemEdges[u]:
                    itemIndegree[v] -= 1
                    groupEdgeCount[gi] -= 1
                    if itemIndegree[v] == 0:
                        queue.append(v)
            if groupEdgeCount[gi]:
                print('Unable to topo sort group', gi)
                return []
        print(soln)
        return soln



def check(topoSort, beforeItems):
    seen = set()
    for item in topoSort:
        for bitem in beforeItems[item]:
            if bitem not in seen:
                print(bitem, 'must appear before', item)
                return False
        seen.add(item)
    return True


def test_1():
    n = 8
    m = 2
    group = [-1,-1,1,0,0,1,0,-1]
    beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    expected = [6,3,4,1,5,2,0,7]
    result = Solution().sortItems(n, m, group, beforeItems)
    # assert result == expected
    assert check(result, beforeItems)


def test_2():
    n = 8
    m = 2
    group = [-1,-1,1,0,0,1,0,-1]
    beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
    result = Solution().sortItems(n, m, group, beforeItems)
    assert result == []
    # assert check(result, beforeItems)


def test_3():
    "WA"
    n = 5
    m = 3
    group = [0,0,2,1,0]
    beforeItems = [[3],[],[],[],[1,3,2]]
    expected = [3,2,0,1,4]
    assert check(expected, beforeItems)
    print(f'groups of solution:', [group[i] for i in expected])
    result = Solution().sortItems(n, m, group, beforeItems)
    assert result != []
    assert check(result, beforeItems)