"""
LeetCode
1261. Find Elements in a Contaminated Binary Tree
February 2025 Challenge
jramaswami
"""


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values_seen = set()
        self._rec(root, 0)
    
    def _rec(self, node, value):
        if node is None:
            return
        self.values_seen.add(value)
        self._rec(node.left, (2 * value) + 1)
        self._rec(node.right, (2 * value) + 2)
        
    def find(self, target: int) -> bool:
        return target in self.values_seen
