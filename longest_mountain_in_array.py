"""
LeetCode: 845. Longest Mountain in Array

https://leetcode.com/contest/weekly-contest-87/problems/longest-mountain-in-array/

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that
        B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
"""

class Solution:
    "Solver."
    def longestMountain(self, seq):
        "Return the length of the longest mountain in seq."
        INIT = 0
        CLIMB = 1
        DESC = 2
        answer = 0
        if len(seq) < 3:
            return answer
        state = INIT
        curr_length = 0
        index = 0
        while index < len(seq) - 1:
            prv = seq[index]
            nxt = seq[index+1]
            if state == INIT:
                if prv < nxt:
                    state = CLIMB
                    curr_length = 2
            elif state == CLIMB:
                if prv < nxt:
                    curr_length += 1
                elif prv > nxt:
                    curr_length += 1
                    state = DESC
                else:
                    state = INIT
                    curr_length = 0
            else:
                if prv < nxt:
                    answer = max(answer, curr_length)
                    curr_length = 2
                    state = CLIMB
                elif prv > nxt:
                    curr_length += 1
                else:
                    answer = max(answer, curr_length)
                    curr_length = 0
                    state = INIT
            index += 1

        if state == DESC:
            answer = max(answer, curr_length)

        if answer >= 3:
            return answer
        return 0

def test1():
    "Sample test 1."
    solver = Solution()
    assert solver.longestMountain([2, 1, 4, 7, 3, 2, 5]) == 5

def test2():
    "Sample test 2."
    solver = Solution()
    assert solver.longestMountain([2, 2, 2]) == 0

def test3():
    "Got WA."
    solver = Solution()
    assert solver.longestMountain([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 11

def test4():
    "Got WA."
    solver = Solution()
    assert solver.longestMountain([0, 1, 0]) == 3
