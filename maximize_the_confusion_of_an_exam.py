"""
LeetCode
2024. Maximize the Confusion of an Exam
July 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        soln = 0

        # Sliding window for F
        window = collections.deque()
        curr_changes = 0
        for answer in answerKey:
            if answer == 'T':
                curr_changes += 1
            window.append(answer)
            while curr_changes > k:
                if window[0] == 'T':
                    curr_changes -= 1
                window.popleft()
            soln = max(soln, len(window))

        # Sliding window for T
        window = collections.deque()
        curr_changes = 0
        for answer in answerKey:
            if answer == 'F':
                curr_changes += 1
            window.append(answer)
            while curr_changes > k:
                if window[0] == 'F':
                    curr_changes -= 1
                window.popleft()
            soln = max(soln, len(window))

        return soln