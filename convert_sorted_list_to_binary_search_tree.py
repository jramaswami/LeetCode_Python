"""
Leet Code :: May 2021 Challenge :: Convert Sorted List to Binary Search Tree
jramaswami
"""
from typing import *
from collections import deque
from leetcode_bst import *
from leetcode_linked_lists import *


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        values = deque()
        while head is not None:
            values.append(head.val)
            head = head.next
        mid = len(values) // 2
        mid_node = TreeNode(values[mid])
        left_node = None
        for i in range(mid):
            new_node = TreeNode(values[i])
            new_node.left = left_node
            left_node = new_node
        mid_node.left = left_node
        right_node = mid_node
        for i in range(mid+1, len(values)):
            new_node = TreeNode(values[i])
            right_node.right = new_node
            right_node = new_node
        return mid_node

# WA [0,1,2,3,4,5]