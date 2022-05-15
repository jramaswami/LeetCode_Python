"""
LeetCode :: May 2022 Challenge :: Deepest Leaves Sum
jramaswami
"""


import collections


class Solution:
    def deepestLeavesSum(self, root):
        sums = []
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            while len(sums) <= level:
                sums.append(0)
            sums[level] += node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return sums[-1]