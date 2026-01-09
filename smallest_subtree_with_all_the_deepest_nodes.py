"""
LeetCode
865. Smallest Subtree with all the Deepest Nodes
January 2026 Challenge
jramaswami
"""


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parents = dict()
        depths = dict()
        nodes = dict()

        def rec(node, parent, depth):
            if node is None:
                return

            depths[node.val] = depth
            parents[node.val] = parent
            nodes[node.val] = node
            rec(node.left, node.val, depth+1)
            rec(node.right, node.val, depth+1)

        rec(root, None, 0)
        max_depth = max(depths.values())
        curr_queue = set(k for k, v in depths.items() if v == max_depth)
        next_queue = set()
        while len(curr_queue) > 1:
            for u in curr_queue:
                next_queue.add(parents[u])
            curr_queue, next_queue = next_queue, set()
        lca = curr_queue.pop()
        return nodes[lca]