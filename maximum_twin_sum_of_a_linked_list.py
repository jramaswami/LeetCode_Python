"""
LeetCode
2130. Maximum Twin Sum of a Linked List
June 2026 Challenge
jramaswami
"""


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        INF = pow(10, 10)
        soln = -INF
        slow = head
        fast = head
        values = []
        while slow:
            if fast:
                values.append(slow.val)
                slow = slow.next
                fast = fast.next
                fast = fast.next
            else:
                soln = max(soln, values.pop() + slow.val)
                slow = slow.next
        return soln