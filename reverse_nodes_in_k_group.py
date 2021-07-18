"""
LeetCode :: July 2021 Challenge :: Reverse Nodes in k-Group
jramaswami
"""


class Solution:
    def reverseKGroup(self, head, k):
        def traverse(node, parent, k0):
            if node is None:
                if k == 0:
                    return (True, None, None)
                else:
                    return (False, None, None)

            reverse_prev, next_head, prev_head = traverse(node.next, node, (k0 + 1)  % k)
            reverse_curr = reverse_prev

            if k0 == 0:
                # I am the tail of the k-group.  I should connect to the head
                # of the previous k-group.
                if reverse_curr:
                    node.next = prev_head
                else:
                    # Leave my link to next.
                    pass
            elif k0 < k - 1 and next_head is not None:
                # If I am in the middle of a k-group and there is a next head,
                # we are reversing this list part of the list.
                if reverse_curr:
                    node.next = parent
            elif k0 == k - 1:
                # If k0 == k - 1 then I am the new head of this k-group.
                next_head, prev_head = node, next_head
                # If there is no previous head, the preceding k-group was not
                # reversed.  So the previous head should just be the current
                # node's next.
                if prev_head is None:
                    prev_head = node.next
                # I am also still being reversed.
                node.next = parent
                # I start the reversing of everything after me.
                reverse_curr = True

            return reverse_curr, next_head, prev_head


        # Corner case: if k is one we are not reversing the list.
        if k == 1:
            return head

        _, next_head, _= traverse(head, None, 0)
        return next_head


#
# Testing
#
from leetcode_linked_lists import *


def node_val(node):
    if node is None:
        return "None"
    return node.val

def test_1():
    head = [1,2,3,4,5]
    k = 2
    expected = [2,1,4,3,5]
    result = Solution().reverseKGroup(make_list(head), k)
    assert make_arr(result) == expected


def test_2():
    head = [1,2,3,4,5]
    k = 3
    expected = [3,2,1,4,5]
    result = Solution().reverseKGroup(make_list(head), k)
    assert make_arr(result) == expected


def test_3():
    head = [1,2,3,4,5]
    k = 1
    expected = [1,2,3,4,5]
    result = Solution().reverseKGroup(make_list(head), k)
    assert make_arr(result) == expected


def test_4():
    head = [1]
    k = 1
    expected = [1]
    result = Solution().reverseKGroup(make_list(head), k)
    assert make_arr(result) == expected


def test_5():
    head = make_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 10
    expected =[10, 9, 8, 7,6,5,4,3,2,1]
    result = Solution().reverseKGroup(head, k)
    assert make_arr(result) == expected


def test_6():
    head = make_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 5
    expected = [5,4,3,2,1,10,9,8,7,6]
    result = Solution().reverseKGroup(head, k)
    assert make_arr(result) == expected
