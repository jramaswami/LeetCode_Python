"""
LeetCode :: March 2022 Challenge :: 2. Add Two Numbers
jramaswami
"""


from leetcode_linked_lists import *


class Solution:

    def addTwoNumbers(self, list1, list2):
        dummy = ListNode(0)

        def get_val(node):
            if node:
                return node.val
            return 0

        def get_next(node):
            if node:
                return node.next
            return None

        curr1 = list1
        curr2 = list2
        curr3 = dummy
        carry = 0
        while curr1 or curr2:
            a = get_val(curr1)
            b = get_val(curr2)
            carry, t = divmod(a + b + carry, 10)
            curr3.next = ListNode(t)
            curr1 = get_next(curr1)
            curr2 = get_next(curr2)
            curr3 = get_next(curr3)
        if carry:
            curr3.next = ListNode(carry)

        return dummy.next


def test_1():
    l1 = [2,4,3]
    l2 = [5,6,4]
    expected = [7,0,8]
    result = Solution().addTwoNumbers(make_list(l1), make_list(l2))
    assert make_arr(result) == expected


def test_2():
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    expected = [8,9,9,9,0,0,0,1]
    result = Solution().addTwoNumbers(make_list(l1), make_list(l2))
    assert make_arr(result) == expected


def test_3():
    l1 = [0]
    l2 = [0]
    expected = [0]
    result = Solution().addTwoNumbers(make_list(l1), make_list(l2))
    assert make_arr(result) == expected
