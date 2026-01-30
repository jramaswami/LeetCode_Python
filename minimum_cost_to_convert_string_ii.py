"""
LeetCode
2977. Minimum Cost to Convert String II
January 2026 Challenge
jramaswami

REF: https://algo.monster/liteproblems/2977
"""


import functools
import math


class TrieNode:
    __slots__ = ['children', 'word_id']

    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word_id = -1


class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        num_transformations = len(cost)
        max_nodes = num_transformations * 2
        graph = [[math.inf for _ in range(max_nodes)] for _ in range(max_nodes)]
        for i in range(max_nodes):
            graph[i][i] = 0

        trie_root = TrieNode()
        word_counter = 0

        def insert_word(word):
            nonlocal word_counter
            current_node = trie_root
            for char in word:
                char_index = ord(char) - ord('a')
                if current_node.children[char_index] is None:
                    current_node.children[char_index] = TrieNode()
                current_node = current_node.children[char_index]
            if current_node.word_id < 0:
                current_node.word_id = word_counter
                word_counter += 1

            return current_node.word_id

        @functools.cache
        def find_min_cost(position):
            # Base case
            if position >= len(source):
                return 0

            # Skip current position if characters already match
            result = math.inf
            if source[position] == target[position]:
                result = find_min_cost(position+1)

            # Try all possible substring replacements
            source_node = trie_root
            target_node = trie_root
            for end_pos in range(position, len(source)):
                source_char_index = ord(source[end_pos]) - ord('a')
                target_char_index = ord(target[end_pos]) - ord('a')
                source_node = source_node.children[source_char_index]
                target_node = target_node.children[target_char_index]
                # Stop if path doesn't exist
                if source_node is None or target_node is None:
                    break
                # Skip if either substring is not a complete word
                if source_node.word_id < 0 or target_node.word_id < 0:
                    continue
                # Recurse with this transformation
                transformation_cost = graph[source_node.word_id][target_node.word_id]
                result = min(result, find_min_cost(end_pos+1) + transformation_cost)

            return result

        # Build graph
        for orig_str, changed_str, trans_cost in zip(original, changed, cost):
            orig_id = insert_word(orig_str)
            changed_id = insert_word(changed_str)
            graph[orig_id][changed_id] = min(graph[orig_id][changed_id], trans_cost)
        # Floyd Warshall for shortest path all pairs
        for k in range(word_counter):
            for i in range(word_counter):
                if graph[i][k] >= math.inf:
                    continue
                for j in range(word_counter):
                    if graph[i][k] + graph[k][j] < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

        min_cost = find_min_cost(0)
        return -1 if min_cost >= math.inf else min_cost


def test_1():
    source = "abcd"
    target = "acbe"
    original = ["a","b","c","c","e","d"]
    changed = ["b","c","b","e","b","e"]
    cost = [2,5,5,1,2,20]
    expected = 28
    assert Solution().minimumCost(source, target, original, changed, cost) == expected