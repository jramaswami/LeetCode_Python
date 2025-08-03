"""
LeetCode
2106. Maximum Fruits Harvested After at Most K Steps
August 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # You can start right or left, harvesting fruite the return to origin
        # You can continue the opposite direction if you have steps left

        # Divide fruits relative to startPos
        left_fruits = []
        right_fruits = []
        initial_fruits_harvested = 0
        for position, fruit_count in fruits:
            if position < startPos:
                left_fruits.append((position, fruit_count))
            elif position > startPos:
                right_fruits.append((position, fruit_count))
            else:
                initial_fruits_harvested += fruit_count
        left_fruits = left_fruits[::-1]

        # Create prefix sums for left and right sides
        left_prefix = []
        fruits_harvested = 0
        for position, fruit_count in left_fruits:
            fruits_harvested += fruit_count
            steps = abs(position - startPos)
            left_prefix.append((steps, fruits_harvested))

        right_prefix = []
        fruits_harvested = 0
        steps = 0
        for position, fruit_count in right_fruits:
            fruits_harvested += fruit_count
            steps = abs(position - startPos)
            right_prefix.append((steps, fruits_harvested))

        soln = initial_fruits_harvested

        # Go left, return to starting position, then go right
        for steps_to_left, fruits_harvested_left in left_prefix:
            if steps_to_left > k:
                break
            steps_to_origin = 2 * steps_to_left
            steps_remaining = k - steps_to_origin
            fruits_harvested_right = 0
            for steps_to_right, fruits_harvested in right_prefix:
                if steps_to_right > steps_remaining:
                    break
                fruits_harvested_right = fruits_harvested
            soln = max(soln, initial_fruits_harvested + fruits_harvested_left + fruits_harvested_right)

        # Go right, return to starting position, then go left
        for steps_to_right, fruits_harvested_right in right_prefix:
            if steps_to_right > k:
                break
            steps_to_origin = 2 * steps_to_right
            steps_remaining = k - steps_to_origin
            fruits_harvested_left = 0
            for steps_to_left, fruits_harvested in left_prefix:
                if steps_to_left > steps_remaining:
                    break
                fruits_harvested_left = fruits_harvested
            soln = max(soln, initial_fruits_harvested + fruits_harvested_left + fruits_harvested_right)

        return soln