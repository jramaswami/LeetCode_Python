"""
Leet Code :: May 2021 Challenge :: Convert Sorted List to Binary Search Tree
jramaswami
"""
from typing import *
from leetcode_bst import *
from leetcode_linked_lists import *


def solve(values, left, right):
    if left > right:
        return None
    if left == right:
        return TreeNode(values[left])
    mid = int(round((left + right) / 2))
    node = TreeNode(values[mid])
    node.left = solve(values, left, mid-1)
    node.right = solve(values, mid+1, right)
    return node


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        return solve(values, 0, len(values) - 1)