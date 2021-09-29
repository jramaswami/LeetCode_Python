"""
LeetCode :: September 2021 Challenge :: Split Linked List in Parts
jramaswami
"""


from leetcode_linked_lists import make_list, make_arr, ListNode


class Solution:

    def splitListToParts(self, head, k):

        def list_length(node):
            if node is None:
                return 0
            return 1 + list_length(node.next)

        L = list_length(head)
        q, r = divmod(L, k)
        node_count = [q if i >= r else q + 1 for i in range(k)]

        soln = []
        curr = head
        for i, n in enumerate(node_count):
            new_head = curr
            new_tail = None
            for _ in range(n):
                new_tail = curr
                curr = curr.next
            if new_tail:
                new_tail.next = None
            soln.append(new_head)
        return soln


#
# Testing
#


null = None


def test_1():
    head = make_list([1,2,3])
    k = 5
    expected = [[1],[2],[3],[],[]]
    result = [make_arr(l) for l in Solution().splitListToParts(head, k)]
    assert result == expected


def test_2():
    head = make_list([1,2,3,4,5,6,7,8,9,10])
    k = 3
    expected = [[1,2,3,4],[5,6,7],[8,9,10]]
    result = [make_arr(l) for l in Solution().splitListToParts(head, k)]
    assert result == expected
