"""
LeetCode :: October 2022 Challenge :: 237. Delete Node in a Linked List
jramaswami
"""


class Solution:
    def deleteNode(self, node):
        # Base case: if next node is None return True
        # because my parent should delete me.
        if node.next is None:
            return True
        # Take value from next node.
        node.val = node.next.val
        if self.deleteNode(node.next):
            node.next = None