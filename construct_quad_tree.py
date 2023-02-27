"""
LeetCode
427. Construct Quad Tree
February 2023 Challenge
jramaswami
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def rec(top_row, bottom_row, left_col, right_col):
            # Base Case: am I a leaf?
            if top_row == bottom_row:
                return Node(grid[top_row][left_col], True, None, None, None, None)

            mid_row = top_row + ((bottom_row - top_row) // 2)
            mid_col = left_col + ((right_col - left_col) // 2)

            top_left_child = rec(top_row, mid_row, left_col, mid_col)
            top_right_child = rec(top_row, mid_row, mid_col+1, right_col)
            bottom_left_child = rec(mid_row+1, bottom_row, left_col, mid_col)
            bottom_right_child = rec(mid_row+1, bottom_row, mid_col+1, right_col)

            if (top_left_child.val == top_right_child.val == bottom_left_child.val == bottom_right_child.val and
                top_left_child.isLeaf and top_right_child.isLeaf and bottom_left_child.isLeaf and bottom_right_child.isLeaf):
                # If all my children are the same, then I am a leaf with their value.
                return Node(top_left_child.val, True, None, None, None, None)
            else:
                # If my children differ, I am a node with val of 0 and all my children.
                return Node(0, False, top_left_child, top_right_child, bottom_left_child, bottom_right_child)

        return rec(0, len(grid)-1, 0, len(grid[0])-1)