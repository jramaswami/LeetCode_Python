"""
LeetCode :: 222. Count Complete Tree Nodes
November 2022 Challenge
jramaswami
"""

class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None:
            return 1

        if root.right is None:
            return 2

        ht = 0
        node = root
        while node:
            ht += 1
            node = node.left

        # There are ht - 1 links to the bottom.
        # This translates into ht - 1 bits.
        lo = 0
        hi = pow(2, ht - 1) - 1
        result = -1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            node = root
            for bit in range(ht - 2, -1, -1):
                mask = 1 << bit
                if mid & mask:
                    node = node.right
                else:
                    node = node.left
            if node is None:
                hi = mid - 1
            else:
                lo = mid + 1
                result = max(result, mid)

        # There are result + 1 nodes on the bottom row.
        bottom_nodes = result + 1
        top_nodes = pow(2, ht - 1) - 1
        return bottom_nodes + top_nodes
