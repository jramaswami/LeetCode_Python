"""
LeetCode
781. Rabbits in Forest
April 2025 Challenge
jramaswami
"""


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # If x is the number a rabbit said share their color
        # then there must be x+1 rabbits that said the same.
        # These x+1 rabbits share the same color.
        # We can sort the answers. Then go through the list,
        # ignoring rabbits that can be the same color as a
        # previous rabbit.
        # O(n log n)
        answers.sort()
        soln = 0
        rabbits_left = 0
        prev_rabit = 0
        # O(n)
        for curr_rabbit in answers:
            # Conditions to add to solution and change rabbit
            if rabbits_left == 0 or prev_rabbit != curr_rabbit:
                soln += (curr_rabbit + 1)
                prev_rabbit = curr_rabbit
                rabbits_left = curr_rabbit
            else:
                rabbits_left -= 1
        return soln