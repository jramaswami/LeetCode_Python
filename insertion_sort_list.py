"""
LeetCode :: December 2021 Challenge :: 147. Insertion Sort List
jramaswami
"""


class Solution:

    def insertionSortList(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        for i in range(1, len(arr)):
            x = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > x:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = x

        new_head = ListNode(arr[0])
        curr = new_head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return new_head
