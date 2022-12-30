"""
LeetCode
797. All Paths From Source to Target
December 2022 Challenge
jramaswami
"""


class Solution:
    def allPathsSourceTarget(self, graph):
        soln = []
        path = []

        def dfs(u):
            path.append(u)
            if u == len(graph) - 1:
                soln.append(list(path))
            for v in graph[u]:
                dfs(v)
            path.pop()

        dfs(0)
        return soln


def test_1():
    graph = [[1,2],[3],[3],[]]
    expected = [[0,1,3],[0,2,3]]
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(expected)


def test_2():
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    expected = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(expected)


def test_3():
    graph = [[1],[]]
    expected = [[0,1]]
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(expected)


def test_4():
    graph = [[1,2,3],[2],[3],[]]
    expected = [[0,1,2,3],[0,2,3],[0,3]]
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(expected)


def test_5():
    graph = [[1,3],[2],[3],[]]
    expected = [[0,1,2,3],[0,3]]
    assert sorted(Solution().allPathsSourceTarget(graph)) == sorted(expected)
