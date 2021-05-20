"""
LeetCode :: May 2021 Challenge :: Binary Tree Level Order Traversal
jramaswami
"""
def solve(node, level, acc):
    if node is None:
        return
    while level >= len(acc):
        acc.append([])
    acc[level].append(node.val)
    solve(node.left, level + 1, acc)
    solve(node.right, level + 1, acc)   

    
class Solution:
    def levelOrder(self, root):
        acc = []
        solve(root, 0, acc)
        return acc

