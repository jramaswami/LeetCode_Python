"""
Leet Code :: November Challenge :: Day 1 :: Convert Binary Number in a Linked List to Integer
https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3516/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        soln = 0
        while head is not None:
            print(head.val)
            soln *= 2
            soln += head.val
            head = head.next
        return soln


def convert_array(arr):
    if arr:
        head = ListNode(arr[0])
        tail = head
        for val in arr[1:]:
            new_tail = ListNode(val)
            tail.next = new_tail
            tail = new_tail
        return head
    else:
        return None


def test_1():
    head = convert_array([1,0,1])
    solver = Solution()
    assert solver.getDecimalValue(head) == 5


def test_2():
    head = convert_array([0])
    solver = Solution()
    assert solver.getDecimalValue(head) == 0


def test_3():
    head = convert_array([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
    solver = Solution()
    assert solver.getDecimalValue(head) == 18880


def test_4():
    head = convert_array([0, 0])
    solver = Solution()
    assert solver.getDecimalValue(head) == 0
