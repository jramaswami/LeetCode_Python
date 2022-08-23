"""
LeetCode :: August 2022 Challenge :: Palindrome Linked List
jramaswami
"""


from typing import *
from leetcode_linked_lists import *


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def traverse(node, head):
            if node is None:
                return True, head

            t, b = traverse(node.next, head)
            return (t and node.val == b.val), b.next

        return traverse(head, head)[0]


def test_1():
    head = make_list([1, 2, 2, 1])
    assert Solution().isPalindrome(head) == True


def test_2():
    head = make_list([1, 2])
    assert Solution().isPalindrome(head) == False


def test_3():
    head = make_list([1, 2, 7, 2, 1])
    assert Solution().isPalindrome(head) == True


def test_4():
    head = make_list([1, 2, 3, 4, 5])
    assert Solution().isPalindrome(head) == False