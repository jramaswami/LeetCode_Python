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

        def khans_algorith(graph):
            "Return the topological sort of the given graph."
            # Compute indegree and number of edges
            edgecount = 0
            indegree = {i: 0 for i in graph}
            for u in graph:
                for v in graph[u]:
                    indegree[v] += 1
                    edgecount += 1

            queue = collections.deque((u for u, d in indegree.items() if d == 0))
            toposort = []
            while queue:
                u = queue.popleft()
                toposort.append(u)
                for v in graph[u]:
                    # Remove edge
                    edgecount -= 1
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            if edgecount == 0:
                return toposort
            return []

        # Assign each of the -1 groups a unique group number
        for i, g in enumerate(group):
            if g == -1:
                group[i] = groupCount
                groupCount += 1

        # Create graph of group dependencies
        group_graph = {i: [] for i in range(groupCount)}
        for item in range(itemCount):
            item_group = group[item]
            for before_item in beforeItems[item]:
                before_item_group = group[before_item]
                if item_group != before_item_group:
                    # before_item_group must come before item_group
                    group_graph[before_item_group].append(item_group)

        # Topologically sort by group
        group_toposort = khans_algorith(group_graph)
        if not group_toposort:
            return []
        print('group toposort=', group_toposort)

        # Place each item in its group
        groups = [[] for _ in range(groupCount)]
        for item, group_index in enumerate(group):
            groups[group_index].append(item)

        print('group', group)
        print('groups', groups)
        # Topologically sort each group
        soln = []
        for group_index in group_toposort:
            # Create graph of intergroup dependencies
            item_graph = {i: [] for i in groups[group_index]}
            for item in groups[group_index]:
                for before_item in beforeItems[item]:
                    before_item_group = group[before_item]
                    if before_item_group == group_index:
                        # before_item must come before item
                        item_graph[before_item].append(item)

            print('item graph for group', group_index, item_graph)
            item_topo = khans_algorith(item_graph)
            if item_topo == []:
                return []
            print('item topo for group', group_index, item_topo)
            soln.extend(item_topo)
        print('soln', soln)
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
    assert result != []
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


def test_4():
    "WA"
    n = 5
    m = 5
    group = [2,0,-1,3,0]
    beforeItems = [[2,1,3],[2,4],[],[],[]]
    result = Solution().sortItems(n, m, group, beforeItems)
    expected = [3,2,4,1,0]
    assert check(expected, beforeItems)
    assert result != []
    assert check(result, beforeItems)