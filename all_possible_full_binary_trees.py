"""
LeetCode
894. All Possible Full Binary Trees
July 2023 Challenge
jramaswami
"""


from collections import deque
from typing import List, Optional


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def build(t):
            queue = deque()
            root = TreeNode(0)
            queue.append((1, root))
            while queue:
                i, node = queue.popleft()
                if t[i*2] != 0:
                    node.left = TreeNode(0)
                    node.right = TreeNode(0)
                    queue.append((i * 2, node.left))
                    queue.append(((i * 2) + 1, node.right))
            return root


        def rec(k, t, z, soln):
            if k < 0:
                return

            if k == 0:
                print(t[:20])
                soln.append(build(t))
                return

            for i, x in enumerate(t[z+1:], start=z+1):
                if x != 0 and t[i * 2] == 0:
                    # Add children at x
                    t[i * 2] = i * 2
                    t[(i * 2) + 1] = (i * 2) + 1
                    rec(k-2, t, i, soln)
                    t[i * 2] = 0
                    t[(i * 2) + 1] = 0

        soln = []
        t = [0 for _ in range(5000)]
        t[1] = 1
        rec(n - 1, t, 0, soln)
        return soln