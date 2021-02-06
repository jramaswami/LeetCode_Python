"""
LeetCode :: Binary Tree Right Side View
jramaswami
"""
def solve(node, level, acc):
    if node is None:
        return
    
    # Preorder: node, left, right
    if level >= len(acc):
        acc.append(node.val)
    else:
        acc[level] = node.val
    
    solve(node.left, level + 1, acc)
    solve(node.right, level + 1, acc)
    
    
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        acc = []
        solve(root, 0, acc)
        return acc
