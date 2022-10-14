"""
LeetCode :: December 2022 Challenge :: 2095. Delete the Middle Node of a Linked List
jramaswami
"""


class Solution:

    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        # Fast/slow pointer
        slow = head
        fast = head.next
        while fast is not None:
            fast = fast.next
            if fast:
                fast = fast.next
            if fast:
                slow = slow.next
        # Delete slow.next
        slow.next = slow.next.next
        return head


#
# Testing
#


import leetcode_linked_lists as lll


def test_1():
    head = [1,3,4,7,1,2,6]
    expected = [1,3,4,1,2,6]
    assert lll.make_arr(Solution().deleteMiddle(lll.make_list(head))) == expected


def test_2():
    head = [1,2,3,4]
    expected = [1,2,4]
    assert lll.make_arr(Solution().deleteMiddle(lll.make_list(head))) == expected


def test_3():
    head = [2,1]
    expected = [2]
    assert lll.make_arr(Solution().deleteMiddle(lll.make_list(head))) == expected


def test_4():
    head = [2]
    expected = []
    assert lll.make_arr(Solution().deleteMiddle(lll.make_list(head))) == expected