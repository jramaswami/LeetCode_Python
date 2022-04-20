"""
LeetCode :: April 2022 Challenge :: 173. Binary Search Tree Iterator
jramaswami
"""


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        if root is None:
            self.curr is None
        else:
            self.generator = self._inorder(root)
            try:
                self.curr = next(self.generator)
            except StopIteration:
                self.curr = None

    def next(self) -> int:
        x = self.curr
        try:
            self.curr = next(self.generator)
        except StopIteration:
            self.curr = None
        return x

    def hasNext(self) -> bool:
        return self.curr is not None

    def _inorder(self, node):
        if node.left:
            yield from self._inorder(node.left)
        yield node.val
        if node.right:
            yield from self._inorder(node.right)
