"""
LeetCode
1361. Validate Binary Tree Nodes
October 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        inDegree = [0 for _ in leftChild]
        edgeCount = 0
        for u, v in enumerate(leftChild):
            if v != -1:
                inDegree[v] += 1
                edgeCount += 1
        for u, v in enumerate(rightChild):
            if v != -1:
                inDegree[v] += 1
                edgeCount += 1

        # Binary tree will have only one element with an indegree of zero.
        if inDegree.count(0) != 1:
            return False
        # All other elements should have an indegree of 1
        if inDegree.count(1) != n-1:
            return False
        # Binary tree will have N-1 edges.
        if edgeCount != n-1:
            return False

        # Each node should be visited once.
        root = inDegree.index(0)
        visited = [False for _ in inDegree]
        queue = collections.deque()
        queue.append(root)
        while queue:
            u = queue.popleft()
            if visited[u]:
                return False
            visited[u] = True
            if leftChild[u] != -1:
                queue.append(leftChild[u])
            if rightChild[u] != -1:
                queue.append(rightChild[u])

        return all(visited)




def test_1():
    n = 4
    leftChild = [1,-1,3,-1]
    rightChild = [2,-1,-1,-1]
    expected = True
    assert Solution().validateBinaryTreeNodes(n, leftChild, rightChild) == expected


def test_2():
    n = 4
    leftChild = [1,-1,3,-1]
    rightChild = [2,3,-1,-1]
    expected = False
    assert Solution().validateBinaryTreeNodes(n, leftChild, rightChild) == expected


def test_3():
    n = 2
    leftChild = [1,0]
    rightChild = [-1,-1]
    expected = False
    assert Solution().validateBinaryTreeNodes(n, leftChild, rightChild) == expected