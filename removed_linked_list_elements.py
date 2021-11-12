
"""
LeetCode :: November 2021 Challenge :: 203. Remove Linked List Elements
jramaswami
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        def traverse(node, remove):
            if node is None:
                return None
            elif node.val == remove:
                return traverse(node.next, remove)
            else:
                node.next = traverse(node.next, remove)
                return node

        return traverse(head, val)