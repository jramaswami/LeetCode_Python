"""
LeetCode :: January 2022 Challenge :: 382. Linked List Random Node
jramaswami
"""


import random


class Solution:

    def __init__(self, head):
        # Place items in an array. O(N) time, O(N) space.
        self.array = []
        curr = head
        while curr:
            self.array.append(curr.val)
            curr = curr.next

    def getRandom(self):
        return random.choice(self.array)
