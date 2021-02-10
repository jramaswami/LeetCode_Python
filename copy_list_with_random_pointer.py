"""
LeetCode :: Copy List with Random Pointer
jramaswami
"""
from typing import *


null = None


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        n = self.next.val if self.next is not None else 'None'
        r = self.random.val if self.random is not None else 'None'
        return f"Node(val={self.val}, next={n}, random={r})"


def make_list(arr):
    """Make a list from the array."""
    if arr == []:
        return None
    # First make nodes
    nodes = [Node(v[0]) for v in arr]
    # Now link them up.
    prev_node = None
    for node, (_, rnd) in zip(nodes, arr):
        # Link next
        if prev_node:
            prev_node.next = node
        prev_node = node
        # Link random
        if rnd is not None:
            node.random = nodes[rnd]
    return nodes[0]


def make_array(head):
    """Make an array from the list."""
    # Get the index of each node and put it in a dictionary for lookup later.
    node_indices = dict()
    node = head
    index = 0
    while node is not None:
        node_indices[node] = index
        index += 1
        node = node.next

    arr = []
    node = head
    while node is not None:
        i = None
        if node.random is not None:
            i = node_indices[node.random]
        arr.append([node.val, i])
        node = node.next
    return arr


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return make_list(make_array(head))


def test_1():
    head_expected = make_list([[7,null],[13,0],[11,4],[10,2],[1,0]])
    head_result = Solution().copyRandomList(head_expected)
    assert make_array(head_result) == make_array(head_expected)

def test_2():
    head_expected = make_list([[1,1],[2,1]])
    head_result = Solution().copyRandomList(head_expected)
    assert make_array(head_result) == make_array(head_expected)

def test_3():
    head_expected = make_list([[3,null],[3,0],[3,null]])
    head_result = Solution().copyRandomList(head_expected)
    assert make_array(head_result) == make_array(head_expected)

def test_4():
    head_expected = make_list([])
    head_result = Solution().copyRandomList(head_expected)
    assert make_array(head_result) == make_array(head_expected)
