"""
LeetCode
2379. Minimum Recolors to Get K Consecutive Black Blocks
March 2025 Challenge
jramaswami
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding Window
        left = 0
        white_blocks = 0
        soln = len(blocks)
        for right, _ in enumerate(blocks):
            if blocks[right] == 'W':
                white_blocks += 1

            while (right - left + 1) > k:
                if blocks[left] == 'W':
                    white_blocks -= 1
                left += 1
            
            if right - left + 1 == k:
                soln = min(soln, white_blocks)
        return soln   

