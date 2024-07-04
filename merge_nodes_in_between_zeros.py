"""
LeetCode
2181. Merge Nodes in Between Zeros
July 2024 Challenge
jramaswami
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_tail = dummy
        curr_sum = 0
        curr_node = head
        while curr_node:
            if curr_node.val == 0:
                if curr_sum > 0:
                    new_node = ListNode(curr_sum)
                    curr_sum = 0
                    curr_tail.next = new_node
                    curr_tail = new_node
            else:
                curr_sum += curr_node.val

            curr_node = curr_node.next
        
        return dummy.next
