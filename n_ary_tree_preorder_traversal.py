"""
LeetCode :: April 2021 Challenge :: N-ary Tree Preorder Traversal
jramaswami
"""
def preorder0(node, acc):
    """Recursive preorder traversal."""
    if node is None:
        return
    acc.append(node.val)
    for child in node.children:
        preorder0(child, acc)


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        acc = []
        preorder0(root, acc)
        return acc