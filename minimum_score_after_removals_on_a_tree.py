"""
LeetCode
2322. Minimum Score After Removals on a Tree
July 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/2322
"""


import collections
import functools
import operator
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # Create adjacency list for tree
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent, exclude_node):
            """Score tree rooted at given node without following edge to exclude_node
            """
            result = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent and neighbor != exclude_node:
                    result ^= dfs(neighbor, node, exclude_node)
            return result

        total = functools.reduce(operator.xor, nums, 0)
        min_score = pow(10, 10)
        subtree_xor = 0

        def dfs_with_score(node, parent, exclude_node):
            nonlocal total, subtree_xor, min_score
            result = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent and neighbor != exclude_node:
                    subtree_result = dfs_with_score(neighbor, node, exclude_node)
                    result ^= subtree_result
                    remaining_xor = subtree_xor ^ subtree_result
                    rest_of_tree_xor = total ^ subtree_xor
                    max_xor = max(subtree_result, remaining_xor, rest_of_tree_xor)
                    min_xor = min(subtree_result, remaining_xor, rest_of_tree_xor)
                    score_difference = max_xor - min_xor
                    min_score = min(min_score, score_difference)
            return result

        for i, _ in enumerate(nums):
            for j in graph[i]:
                subtree_xor = dfs(i, -1, j)
                dfs_with_score(i, -1, j)
        return min_score