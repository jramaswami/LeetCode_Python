"""
LeetCode :: April 2021 Challenge :: Remove Nth Node From End of List
jramaswami
"""
from leetcode_linked_lists import *
from typing import *


def solve0(node, n):
    """Recursive solution."""
    if node is None:
        return node, 1

    prev, i = solve0(node.next, n)
    if i == n:
        return prev, i + 1
    else:
        node.next = prev
        return node, i + 1

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return solve0(head, n)[0]


def test_1():
    head = [1,2,3,4,5]
    n = 2
    expected = [1,2,3,5]
    result = Solution().removeNthFromEnd(make_list(head), n)
    print(result)
    assert make_arr(result) == expected
    
def test_2():
    head = [1]
    n = 1
    result = Solution().removeNthFromEnd(make_list(head), n)
    expected = []
    print(result)
    assert make_arr(result) == expected

def test_3():
    head = [1,2]
    n = 1
    expected = [1]
    result = Solution().removeNthFromEnd(make_list(head), n)
    print(result)
    assert make_arr(result) == expected
