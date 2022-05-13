"""
LeetCode :: May 2022 Challenge :: 117. Populating Next Right Pointers in Each Node II
jramaswami
"""


import collections



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            Q = collections.deque([(root, 0)])
            while Q:
                node, level = Q.popleft()
                if Q and level == Q[0][1]:
                    node.next = Q[0][0]
                if node.left:
                    Q.append((node.left, level+1))
                if node.right:
                    Q.append((node.right, level+1))
            return root