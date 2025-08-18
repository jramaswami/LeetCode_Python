"""
LeetCode
679. 24 Game
August 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/679
"""


from typing import List


EPS = pow(10, -6)


class Solution:

    def judgePoint24(self, cards: List[int]) -> bool:
        # Convert the input list of integers to a list of floats
        num_list = [float(num) for num in cards]
        # Initiate depth-first search to evaluate all possible results
        return self.dfs(num_list)

    def dfs(self, num_list):
        if not num_list:
            return False
        if len(num_list) == 1:
            return abs(num_list[0] - 24.0) < EPS
        for i, _ in enumerate(num_list):
            for j in range(i+1, len(num_list)):
                for operation in range(6):
                    next_list = self.get_next_list(num_list, i, j, operation)
                    if next_list and self.dfs(next_list):
                        return True
        return False

    def get_next_list(self, num_list, first_index, second_index, operation):
        next_list = [num_list[k] for k in range(len(num_list)) if k != first_index and k != second_index]
        # Perform the operation based on the operation index
        if operation == 0: # Addition
            next_list.append(num_list[first_index] + num_list[second_index])
        elif operation == 1: # Subtraction (first - second)
            next_list.append(num_list[first_index] - num_list[second_index])
        elif operation == 2: # Subtraction (second - first)
            next_list.append(num_list[second_index] - num_list[first_index])
        elif operation == 3: # Multiplication
            next_list.append(num_list[first_index] * num_list[second_index])
        elif operation == 4: # Division (first / second), check for division by zero
            if num_list[second_index] != 0:
                next_list.append(num_list[first_index] / num_list[second_index])
            else:
                return []
        elif operation == 5: # Division (second / first), check for division by zero
            if num_list[first_index] != 0:
                next_list.append(num_list[second_index] / num_list[first_index])
            else:
                return []
        # Return the new list to continue the search
        return next_list


def test_1():
    cards = [4,1,8,7]
    expected = True
    assert Solution().judgePoint24(cards) == expected