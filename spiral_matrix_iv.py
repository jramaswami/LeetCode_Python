"""
LeetCode
2326. Spiral Matrix IV
September 2024 Challenge
jramaswami
"""


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Create the matrix
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dirn = 0

        curr = head
        r = c = 0
        while curr != None:
            # Write value
            matrix[r][c] = curr.val
            # Move to next in linked list
            curr = curr.next
            # Move to next cell in matrix
            dr, dc = offsets[dirn]
            r0, c0 = r + dr, c + dc
            # Turn if the next cell has a value or is out of bounds
            if not inbounds(r0, c0) or matrix[r0][c0] >= 0:
                dirn = (dirn + 1) % len(offsets)
                dr, dc = offsets[dirn]
                r0, c0 = r + dr, c + dc
            r, c = r0, c0
        return matrix
