"""
LeetCode :: March 2022 Challenge :: 21. Merge Two Sorted Lists
jramaswami
"""


class Solution:

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0, None)
        tail = dummy

        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
                tail = tail.next
            else:
                tail.next = curr2
                curr2 = curr2.next
                tail = tail.next
            tail.next = None

        while curr1:
            tail.next = curr1
            curr1 = curr1.next
            tail = tail.next
            tail.next = None

        while curr2:
            tail.next = curr2
            curr2 = curr2.next
            tail = tail.next
            tail.next = None

        return dummy.next
