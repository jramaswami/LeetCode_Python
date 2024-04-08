"""
LeetCode
1700. Number of Students Unable to Eat Lunch
April 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one_students = sum(students)
        zero_students = len(students) - one_students
        for s in sandwiches:
            if s == 0 and zero_students > 0:
                zero_students -= 1
            elif s == 1 and one_students > 0:
                one_students -= 1
            else:
                break
        return one_students + zero_students


def test_1():
    students, sandwiches, expected = [1,1,0,0], [0,1,0,1], 0
    assert Solution().countStudents(students, sandwiches) == expected


def test_2():
    students, sandwiches, expected = [1,1,1,0,0,1], [1,0,0,0,1,1], 3
    assert Solution().countStudents(students, sandwiches) == expected