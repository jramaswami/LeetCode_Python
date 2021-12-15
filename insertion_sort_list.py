"""
LeetCode :: December 2021 Challenge :: 147. Insertion Sort List
jramaswami
"""


class Solution:

    def insertionSortList(self, head):
        sorted_list = None
        unsorted_list = head
        while unsorted_list:
            # Pop the first node off the unsorted list.
            new_node = unsorted_list
            unsorted_list = new_node.next
            # Put that item at the head of the sorted list.
            new_node.next = sorted_list
            sorted_list = new_node
            # Swap that item with the next until it is in the right place.
            curr = sorted_list
            while curr.next:
                if curr.val > curr.next.val:
                    curr.val, curr.next.val = curr.next.val, curr.val
                curr = curr.next
        return sorted_list
