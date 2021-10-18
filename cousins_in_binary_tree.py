"""
LeetCode :: October 2021 Challenge :: 993. Cousins in Binary Tree
jramaswami
"""


class Solver:

    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.x_level = -1
        self.y_level = -1
        self.x_parent = None
        self.y_parent = None

    def solve(self):
        self._traverse(self.root, None, 0)
        return self.x_level == self.y_level and self.x_parent != self.y_parent

    def _traverse(self, node, parent, level):
        if node is None:
            return
        if node.val == self.x:
            self.x_level = level
            self.x_parent = parent

        if node.val == self.y:
            self.y_level = level
            self.y_parent = parent

        self._traverse(node.left, node, level + 1)
        self._traverse(node.right, node, level + 1)


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        solver = Solver(root, x, y)
        return solver.solve()
