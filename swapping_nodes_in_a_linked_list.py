"""
LeetCode :: April 2022 Challenge :: Swapping Nodes in a Linked List
jramaswami
"""


class Solution:
    def swapNodes(self, head, k):
        curr = head
        for _ in range(1, k):
            curr = curr.next
        a = curr

        b = head
        while curr.next is not None:
            curr = curr.next
            b = b.next

        a.val, b.val = b.val, a.val
        return head


#
# Testing
#


from leetcode_linked_lists import *


def test_1():
     head = make_list([1,2,3,4,5])
     k = 2
     assert make_arr(Solution().swapNodes(head, k)) == [1,4,3,2,5]


def test_2():
    head = make_list([1])
    k = 1
    assert make_arr(Solution().swapNodes(head, k)) == [1]


def test_3():
    head = make_list([1,2])
    k = 1
    assert make_arr(Solution().swapNodes(head, k)) == [2, 1]


def test_4():
    head = make_list([1,2,3])
    k = 2
    assert make_arr(Solution().swapNodes(head, k)) == [1, 2, 3]


def test_5():
    head = make_list([100,90])
    k = 2
    assert make_arr(Solution().swapNodes(head, k)) == [90, 100]


def test_6():
    "WA"
    head = make_list([7,9,6,6,7,8,3,0,9,5])
    k = 5
    assert make_arr(Solution().swapNodes(head, k)) == [7,9,6,6,8,7,3,0,9,5]
