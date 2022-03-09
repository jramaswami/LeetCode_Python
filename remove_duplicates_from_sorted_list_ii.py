"""
LeetCode :: March 2022 Challenge :: 82. Remove Duplicates from Sorted List II
jramaswami
"""


from leetcode_linked_lists import *


class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-1000)

        tail = dummy
        curr = head
        while curr:
            candidate = curr
            if candidate.next and candidate.val == candidate.next.val:
                # Discard duplicate values
                while curr and curr.val == candidate.val:
                    curr = curr.next
            else:
                # Append nonduplicate value to new list.
                tail.next = curr
                tail = curr
                curr = curr.next
                tail.next = None
        return dummy.next


def test_1():
    head = [1,2,3,3,4,4,5]
    expected = [1,2,5]
    result = Solution().deleteDuplicates(make_list(head))
    assert make_arr(result) == expected


def test_2():
    head = [1,1,1,2,3]
    expected = [2,3]
    result = Solution().deleteDuplicates(make_list(head))
    assert make_arr(result) == expected


def test_3():
    "WA"
    head = [1,2,2]
    expected = [1]
    result = Solution().deleteDuplicates(make_list(head))
    assert make_arr(result) == expected
