"""
LeetCode :: September 2021 Challenge :: Maximum Length of a Concatenated String with Unique Characters
jramaswami
"""


from collections import defaultdict


class Solution:

    def maxLength(self, arr):
        SOURCE = -1
        SINK = -2

        letter_sets = [set(word) for word in arr]
        def dfs(node, visited, letter_acc, length_acc):
            result = length_acc
            for neighbor, neighbor_word in enumerate(arr):
                neighbor_set = letter_sets[neighbor]
                if neighbor not in visited and letter_acc.isdisjoint(neighbor_set):
                    visited.add(neighbor)
                    result = max(result, dfs(neighbor, visited, letter_acc | neighbor_set, length_acc + len(neighbor_word)))
                    visited.remove(neighbor)
            return result

        visited = set()
        soln = dfs(SOURCE, visited, set(), 0)
        return soln


def test_1():
    arr = ["un","iq","ue"]
    expected = 4
    assert Solution().maxLength(arr) == expected


def test_2():
    arr = ["cha","r","act","ers"]
    expected = 6
    assert Solution().maxLength(arr) == expected


def test_3():
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    expected = 26
    assert Solution().maxLength(arr) == expected


def test_4():
    arr = []
    for c in 'abcdefghijklmnop':
        arr.append(c * 26)
    expected = 26 * 16
    for word in arr:
        print(word)
    assert Solution().maxLength(arr) == expected
    assert False
