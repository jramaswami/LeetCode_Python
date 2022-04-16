"""
LeetCode :: 1367. Linked List in Binary Tree
jramaswami
"""


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def find_head(node, head):
            if node is None:
                return False

            result = False
            if node.val == head.val:
                return (
                    find_list_from(node, head) or
                    find_head(node.left, head) or
                    find_head(node.right, head)
                )
            return find_head(node.left, head) or find_head(node.right, head)

        def find_list_from(node, curr):
            if curr is None:
                return True

            if node is None:
                return False

            if node.val == curr.val:
                return (
                    find_list_from(node.left, curr.next) or
                    find_list_from(node.right, curr.next)
                )
            return False

        return find_head(root, head)
